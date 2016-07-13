#include <stdio.h>
#include "api/mdl_api.h"
#include "api/mdl_shl1_msg.h"
#include "api/mdl_shl2_msg.h"
#include "api/mdl_szl2_msg.h"
#include "api/mdl_szl1_msg.h"
#include "api/mdl_cffex_msg.h"
#include "api/mdl_czce_msg.h"
#include "api/mdl_dce_msg.h"
#include "api/mdl_shfe_msg.h"
#include "api/mdl_hkex_msg.h"
#include "api/mdl_bar_msg.h"

using namespace datayes::mdl;

#if defined(_MSC_VER)
#pragma comment(lib, "mdl_api.lib")
#endif


class MyMessageHandler : public MessageHandler {
public:
	bool Open(const char* address) {
		m_IOManager = CreateIOManager();
		if (m_IOManager.IsNull()) {
			printf("Incompatible API lib version.\n");
			return false;
		}
		
		SubscriberPtr sub = m_IOManager->CreateSubscriber(this);
		sub->SetServerAddress(address);

		//// subscribe level1 msg
		// shanghai level1 new version
		sub->SubcribeMessage<mdl_shl1_msg::Indexes>();
		sub->SubcribeMessage<mdl_shl1_msg::Equity>();
		sub->SubcribeMessage<mdl_shl1_msg::Bonds>();
		sub->SubcribeMessage<mdl_shl1_msg::Funds>();

		sub->SubcribeMessage<mdl_szl1_msg::SZL1Index>();
		sub->SubcribeMessage<mdl_szl1_msg::SZL1Stock>();
		
		// subscribe shanghai minute bar and capitalflow
		//sub->SubcribeMessage<mdl_bar_msg::XSHGCapitalFlow>();
		//sub->SubcribeMessage<mdl_bar_msg::XSHGStockMinuteBar>();
		//sub->SubcribeMessage<mdl_bar_msg::XSHEStockMinuteBar>();

		//// subscribe all futures
		//sub->SubcribeMessage<mdl_dce_msg::CTPFuture>();
		//sub->SubcribeMessage<mdl_czce_msg::CTPFuture>();
		//sub->SubcribeMessage<mdl_shfe_msg::CTPFuture>();
		//sub->SubcribeMessage<mdl_cffex_msg::CTPFuture>();

		//// subscribe hkex msg
		//sub->SubcribeMessage<mdl_hkex_msg::OMDMarketData>();
		//
		//// subscribe sh level2 msg
		//sub->SubcribeMessage<mdl_shl2_msg::SHL2Transaction>();
		//sub->SubcribeMessage<mdl_shl2_msg::SHL2MarketData>();
		//sub->SubcribeMessage<mdl_shl2_msg::SHL2VirtualAuctionPrice>();
		//sub->SubcribeMessage<mdl_shl2_msg::SHL2Index>();
		//sub->SubcribeMessage<mdl_shl2_msg::SHL2MarketOverview>();
		//sub->SubcribeMessage<mdl_shl2_msg::OPTLevel1>();

		//// subscribe sz level2 msg
		//sub->SubcribeMessage<mdl_szl2_msg::SecurityStatus>();
		//sub->SubcribeMessage<mdl_szl2_msg::Bulletin>();
		//sub->SubcribeMessage<mdl_szl2_msg::Snapshot300111_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Snapshot309011_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Snapshot309111_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Snapshot300611_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Order300192_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Order300592_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Order300792_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Transaction300191_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Transaction300591_v2>();
		//sub->SubcribeMessage<mdl_szl2_msg::Transaction300791_v2>();
		
		// connect to server
		std::string err = sub->Connect();
		if (err.empty()) {
			printf("Connect to server successfully.\n");
			return true;
		}
		printf("Connect to server failed: %s.\n", err.c_str());
		return false; 
	}
 
	void Close() {
		if (!m_IOManager.IsNull()) {
			m_IOManager->Shutdown();
		}
	}

	// handle network failure
	virtual void OnMDLAPIMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_api_msg::ConnectingEvent::MessageID) {
			mdl_api_msg::ConnectingEvent* resp = (mdl_api_msg::ConnectingEvent*)msg->GetBody();
			printf("Connect to %s ...\n", resp->Address.c_str());
		}
		else if (head->MessageID == mdl_api_msg::ConnectErrorEvent::MessageID) {
			mdl_api_msg::ConnectErrorEvent* resp = (mdl_api_msg::ConnectErrorEvent*)msg->GetBody();
			printf("Connect to %s failed %s.\n", resp->Address.c_str(), resp->ErrorMessage.c_str());
		}
		else if (head->MessageID == mdl_api_msg::DisconnectedEvent::MessageID) {
			mdl_api_msg::DisconnectedEvent* resp = (mdl_api_msg::DisconnectedEvent*)msg->GetBody();
			printf("Disconnected from %s: %s.\n", resp->Address.c_str(), resp->ErrorMessage.c_str());
		}
	}

	// handle server response
	virtual void OnMDLSysMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_sys_msg::LogonResponse::MessageID) {
			mdl_sys_msg::LogonResponse* resp = (mdl_sys_msg::LogonResponse*)msg->GetBody();
			if (resp->ReturnCode != MDLEC_OK) {
				printf("Logon failed: return code %d.\n", resp->ReturnCode);
			}
			for (uint32_t i = 0; i < resp->Services.Length; ++i) {
				for (uint32_t j = 0; j < resp->Services[i]->Messages.Length; ++j) {
					if (resp->Services[i]->Messages[j]->MessageStatus != MDLEC_OK) {
						printf("The server doesn't publish message (service id %d message id %d)\n", 
							resp->Services[i]->ServiceID,
							resp->Services[i]->Messages[j]->MessageID);
					}
				}
			}
		}
	}

	// print shfe future message
	virtual void OnMDLSHFEMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_shfe_msg::CTPFuture::MessageID) {
			mdl_shfe_msg::CTPFuture* body = (mdl_shfe_msg::CTPFuture*)msg->GetBody();
			PrintFutureMessage(body);
		}
	}

	// print czce future message
	virtual void OnMDLCZCEMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_czce_msg::CTPFuture::MessageID) {
			mdl_czce_msg::CTPFuture* body = (mdl_czce_msg::CTPFuture*)msg->GetBody();
			PrintFutureMessage(body);
		}
	}

	// print cffex future message
	virtual void OnMDLCFFEXMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_cffex_msg::CTPFuture::MessageID) {
			mdl_cffex_msg::CTPFuture* body = (mdl_cffex_msg::CTPFuture*)msg->GetBody();
			PrintFutureMessage(body);
		}
	}

	// print dce future message
	virtual void OnMDLDCEMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_dce_msg::CTPFuture::MessageID) {
			mdl_dce_msg::CTPFuture* body = (mdl_dce_msg::CTPFuture*)msg->GetBody();
			PrintFutureMessage(body);
		}
	}

	// print shanghai level1 message
	virtual void OnMDLSHL1Message(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_shl1_msg::Equity::MessageID) {
			mdl_shl1_msg::Equity* body = (mdl_shl1_msg::Equity*)msg->GetBody(); 
			PrintNewStockMessage(body);
		}
		else if (head->MessageID == mdl_shl1_msg::Indexes::MessageID) {
			mdl_shl1_msg::Indexes* body = (mdl_shl1_msg::Indexes*)msg->GetBody(); 
			PrintIndexMessage(body); 
		}
		else if (head->MessageID == mdl_shl1_msg::Bonds::MessageID) {
			mdl_shl1_msg::Bonds* body = (mdl_shl1_msg::Bonds*)msg->GetBody(); 
			PrintNewStockMessage(body);
		}
		else if (head->MessageID == mdl_shl1_msg::Funds::MessageID) {
			mdl_shl1_msg::Funds* body = (mdl_shl1_msg::Funds*)msg->GetBody(); 
			PrintNewStockMessage(body);
		}
	}

	// print shenzhen level1 message
	virtual void OnMDLSZL1Message(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_szl1_msg::SZL1Index::MessageID) {
			mdl_szl1_msg::SZL1Index* body = (mdl_szl1_msg::SZL1Index*)msg->GetBody();
			PrintIndexMessage(body); 
		}
		else if (head->MessageID == mdl_szl1_msg::SZL1Stock::MessageID) {
			mdl_szl1_msg::SZL1Stock* body = (mdl_szl1_msg::SZL1Stock*)msg->GetBody();
			PrintStockMessage(body); 
		}
	}

	template <class T> 
	void PrintIndexMessage(const T* msgBody) {
		printf("%d:%02d:%02d %s %s HighIndex:%s LowIndex:%s LastIndex:%s\n",
			msgBody->UpdateTime.GetHour(), msgBody->UpdateTime.GetMinute(), msgBody->UpdateTime.GetSecond(),
			msgBody->IndexID.std_str().c_str(), msgBody->IndexName.std_str().c_str(), 
			DoubleToString(msgBody->HighIndex).c_str(), 
			DoubleToString(msgBody->LowIndex).c_str(), 
			DoubleToString(msgBody->LastIndex).c_str());
	}
	template <class T> 
	void PrintNewStockMessage(const T* msgBody) {
		printf("%d:%02d:%02d %s %s HighPrice:%s LowPrice:%s LastPrice:%s\n",
			msgBody->UpdateTime.GetHour(), msgBody->UpdateTime.GetMinute(), msgBody->UpdateTime.GetSecond(),
			msgBody->SecurityID.std_str().c_str(), msgBody->SecurityName.std_str().c_str(), 
			DoubleToString(msgBody->HighPrice).c_str(), 
			DoubleToString(msgBody->LowPrice).c_str(), 
			DoubleToString(msgBody->LastPrice).c_str());
	}
	template <class T> 
	void PrintStockMessage(const T* msgBody) {
		printf("%d:%02d:%02d %s %s HighPrice:%s LowPrice:%s LastPrice:%s\n",
			msgBody->UpdateTime.GetHour(), msgBody->UpdateTime.GetMinute(), msgBody->UpdateTime.GetSecond(),
			msgBody->SecurityID.std_str().c_str(), msgBody->SecurityName.std_str().c_str(), 
			FloatToString(msgBody->HighPrice).c_str(), 
			FloatToString(msgBody->LowPrice).c_str(), 
			FloatToString(msgBody->LastPrice).c_str());
	}

	template <class T> 
	void PrintFutureMessage(const T* msgBody) {
		printf("%d:%02d:%02d %s HighPrice:%s LowPrice:%s LastPrice:%s\n",
			msgBody->UpdateTime.GetHour(), msgBody->UpdateTime.GetMinute(), msgBody->UpdateTime.GetSecond(),
			msgBody->InstruID.std_str().c_str(),
			DoubleToString(msgBody->HighPrice).c_str(),
			DoubleToString(msgBody->LowPrice).c_str(),
			DoubleToString(msgBody->LastPrice).c_str());
	}

	template <class T>
	std::string DoubleToString(const T& mdlDouble) {
		if (mdlDouble.IsNull()) {
			return std::string("null");
		}
		char strBuf[100];
		sprintf(strBuf, "%.2f", mdlDouble.GetDouble());
		return std::string(strBuf);
	}

	template <class T>
	std::string FloatToString(const T& mdlFloat) {
		if (mdlFloat.IsNull()) {
			return std::string("null");
		}
		char strBuf[100];
		sprintf(strBuf, "%.2f", mdlFloat.GetFloat());
		return std::string(strBuf);
	}

	// print hkex message
	virtual void OnMDLHKExMessage(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_hkex_msg::OMDMarketData::MessageID) {
			mdl_hkex_msg::OMDMarketData* body = (mdl_hkex_msg::OMDMarketData*)msg->GetBody();
			printf("[%d:%02d:%02d.%d] %s ",
				body->TradTime.GetHour(), body->TradTime.GetMinute(), body->TradTime.GetSecond(), body->TradTime.GetMilliSec(),
				body->TickerSymbol.c_str());
			if (body->LastPrice.IsNull()) {
				printf("LastPrice:null");
			}
			else {
				printf("LastPrice:%.2f", body->LastPrice.GetFloat());
			}	
			if (body->ChangePct.IsNull()) {
				printf("(),");
			}
			else {
				printf("(%.3f%%),", body->ChangePct.GetFloat() * 100);
			}	
			printf("Volume:%.3fM,", (float)body->Quantity / 1000000.0);
			if (body->Turnover.IsNull()) {
				printf("Turnover:null\n");
			}
			else {
				printf("Turnover:%.3fM\n", body->Turnover.GetDouble() / 1000000.0);
			}	

			if (body->AskBook.Length > 0) {
				if (body->AskBook[0]->Price.IsNull()) {
					printf("	Ask1:null,0,");
				}
				else {
					printf("	Ask1:%.3f,%d,", body->AskBook[0]->Price.GetFloat(), body->AskBook[0]->Volume);
				}
			}
			if (body->BidBook.Length > 0) {
				if (body->BidBook[0]->Price.IsNull()) {
					printf("	Bid1:null,0");
				}
				else {
					printf("	Bid1:%.3f,%d", body->BidBook[0]->Price.GetFloat(), body->BidBook[0]->Volume);
				}
			} 
			printf("\n");
		}
	}
	// handle shenzhen level2 message
	void OnMDLSZL2Message(const MDLMessage* msg) {
		MDLMessageHead* head = msg->GetHead();
		if (head->MessageID == mdl_szl2_msg::Snapshot300111_v2::MessageID) {
			mdl_szl2_msg::Snapshot300111_v2 * resp = (mdl_szl2_msg::Snapshot300111_v2*)msg->GetBody();
			printf("[%d:%02d:%02d] %s %s Hi:%.6f Lo:%.6f Last:%.6f Vol:%lld Tun:%.4f\n",
				resp->UpdateTime.GetHour(), resp->UpdateTime.GetMinute(), resp->UpdateTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->TradingPhaseCode.c_str(),
				resp->HighPrice.GetDouble(), resp->LowPrice.GetDouble(), resp->LastPrice.GetDouble(),
				resp->Volume,
				resp->Turnover.GetDouble());

			for (size_t i = 0; i < 10; ++i) {
				double askPrice = 0.0;
				int64_t askVolumn = 0.0;
				double bidPrice = 0.0;
				int64_t bidVolumn = 0.0;
				if (i < resp->AskPriceLevel.Length) {
					askPrice = resp->AskPriceLevel[i]->Price.GetDouble();
					askVolumn = resp->AskPriceLevel[i]->Volume;
				}
				if (i < resp->BidPriceLevel.Length) {
					bidPrice = resp->BidPriceLevel[i]->Price.GetDouble();
					bidVolumn = resp->BidPriceLevel[i]->Volume;
				}
				printf("%.6f %lld\t\t%.6f %lld\n", askPrice, askVolumn, bidPrice, bidVolumn);
			}
		}
		else if (head->MessageID == mdl_szl2_msg::Order300192_v2::MessageID) {
			mdl_szl2_msg::Order300192_v2 * resp = (mdl_szl2_msg::Order300192_v2*)msg->GetBody();
			printf("[%d:%02d:%02d] %s Side:%d Price:%.4f Qty:%lld\n",
				resp->TransactTime.GetHour(), resp->TransactTime.GetMinute(), resp->TransactTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->Side,
				resp->Price.GetDouble(), resp->OrderQty);
		}
		else if (head->MessageID == mdl_szl2_msg::Transaction300191_v2::MessageID) {
			mdl_szl2_msg::Transaction300191_v2 * resp = (mdl_szl2_msg::Transaction300191_v2*)msg->GetBody();
			printf("[%d:%02d:%02d] %s ET:%d Price:%.4f Qty:%lld\n",
				resp->TransactTime.GetHour(), resp->TransactTime.GetMinute(), resp->TransactTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->ExecType,
				resp->LastPx.GetDouble(), resp->LastQty);
		}
	}

	void OnMDLSHL2Message(const MDLMessage* msg) {
		if (msg->GetHead()->MessageID == mdl_shl2_msg::SHL2Index::MessageID) {
			mdl_shl2_msg::SHL2Index * resp = (mdl_shl2_msg::SHL2Index*)msg->GetBody();
			printf("#%lld [%d:%02d:%02d] %s Hi:%.2f Lo:%.2f Last:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->UpdateTime.GetHour(), resp->UpdateTime.GetMinute(), resp->UpdateTime.GetSecond(),
				resp->SecurityID.std_str().c_str(),  
				resp->HighIndex.GetDouble(), resp->LowIndex.GetDouble(), resp->LastIndex.GetDouble());
		}	
		else if (msg->GetHead()->MessageID == mdl_shl2_msg::SHL2MarketData::MessageID) {
			mdl_shl2_msg::SHL2MarketData * resp = (mdl_shl2_msg::SHL2MarketData*)msg->GetBody();
 			printf("#%lld [%d:%02d:%02d] %s Hi:%.2f Lo:%.2f Last:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->UpdateTime.GetHour(), resp->UpdateTime.GetMinute(), resp->UpdateTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->HighPrice.GetFloat(),	resp->LowPrice.GetFloat(), resp->LastPrice.GetFloat());
		}
		else if (msg->GetHead()->MessageID == mdl_shl2_msg::SHL2MarketOverview::MessageID) {
			mdl_shl2_msg::SHL2MarketOverview * resp = (mdl_shl2_msg::SHL2MarketOverview*)msg->GetBody();
		}
 		else if (msg->GetHead()->MessageID == mdl_shl2_msg::SHL2Transaction::MessageID) {
			mdl_shl2_msg::SHL2Transaction * resp = (mdl_shl2_msg::SHL2Transaction*)msg->GetBody();
		}
 		else if (msg->GetHead()->MessageID == mdl_shl2_msg::SHL2VirtualAuctionPrice::MessageID) {
			mdl_shl2_msg::SHL2VirtualAuctionPrice * resp = (mdl_shl2_msg::SHL2VirtualAuctionPrice*)msg->GetBody();
		}
		else if (msg->GetHead()->MessageID == mdl_shl2_msg::OPTLevel1::MessageID) {
			mdl_shl2_msg::OPTLevel1 * resp = (mdl_shl2_msg::OPTLevel1*)msg->GetBody();
 			printf("#%lld [%d:%02d:%02d] %s Hi:%.2f Lo:%.2f Last:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->UpdateTime.GetHour(), resp->UpdateTime.GetMinute(), resp->UpdateTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->HighPx.GetDouble(),	resp->LowPx.GetDouble(), resp->LastPx.GetDouble());
		}
	}

	virtual void OnMDLBARMessage(const MDLMessage* msg) {
		if (msg->GetHead()->MessageID == mdl_bar_msg::XSHGStockMinuteBar::MessageID) {
			mdl_bar_msg::XSHGStockMinuteBar * resp = (mdl_bar_msg::XSHGStockMinuteBar*)msg->GetBody();
 			printf("#%lld [%d:%02d:%02d] %s Hi:%.2f Lo:%.2f Last:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->BarTime.GetHour(), resp->BarTime.GetMinute(), resp->BarTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->HighPrice.GetDouble(), resp->LowPrice.GetDouble(), resp->LowPrice.GetDouble());
		}
		else if (msg->GetHead()->MessageID == mdl_bar_msg::XSHGCapitalFlow::MessageID) {
			mdl_bar_msg::XSHGCapitalFlow * resp = (mdl_bar_msg::XSHGCapitalFlow*)msg->GetBody();
 			printf("#%lld [%d:%02d:%02d] %s %s Px:%.2f Vol:%lld NetIn:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->TradeTime.GetHour(), resp->TradeTime.GetMinute(), resp->TradeTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->BSFlag == 1 ? "B" : (resp->BSFlag == 2 ? "S" : "NA"),
				resp->Price.GetDouble(), resp->Volume, resp->NetCapitalInflow.GetDouble());
		}
		else if (msg->GetHead()->MessageID == mdl_bar_msg::IndustryCapitalFlow::MessageID) {
			mdl_bar_msg::IndustryCapitalFlow * resp = (mdl_bar_msg::IndustryCapitalFlow*)msg->GetBody();
 			printf("#%lld [%d:%02d:%02d] %s %s In:%.2f OutIn:%.2f NetIn:%.2f\n",
				msg->GetHead()->SequenceID,
				resp->TradeTime.GetHour(), resp->TradeTime.GetMinute(), resp->TradeTime.GetSecond(),
				resp->SecurityID.std_str().c_str(), 
				resp->SecurityName.std_str().c_str(),  
				resp->CapitalInFlow.GetDouble(),
				resp->CapitalOutFlow.GetDouble(),
				resp->NetCapitalInflow.GetDouble());
		}
	}

private:
	IOManagerPtr m_IOManager;
};

///////////////////////////////////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[]) { 
	if (argc != 2) {
		printf("usage: mdl_api_demo server_hostname:port\n");
		return 1;
	}

	MyMessageHandler msgHandler;
	if (msgHandler.Open(argv[1])) {
		printf("Receiving message, press enter to stop.\n");
		getchar();
	}

	msgHandler.Close(); 
	printf("Press enter to exit.\n");
	getchar();
	return 0;
}