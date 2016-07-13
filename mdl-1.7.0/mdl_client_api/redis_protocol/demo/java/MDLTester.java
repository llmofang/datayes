import redis.clients.jedis.BinaryJedisPubSub;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.exceptions.JedisException;

import java.lang.reflect.Method;

/**
 * Created by rui.wang on 2015/10/16.
 *
 */


public class MDLTester {
    public static void main(String args[]){

        //redis host and port
        String host= "feeder01-dev.datayes.com";
        int port=9379;

        try{
            //Connect to Redis
            JedisPoolConfig config = new JedisPoolConfig();
            config.setMaxTotal(150);
            config.setMaxIdle(10);
            config.setMaxWaitMillis(30000);
            config.setTestOnBorrow(true);
            JedisPool pool = new JedisPool(config, host, port, 5000);
            Jedis jedis = pool.getResource();

            //subscribe 上交所Level1 股票数据
            String channel= "mdl.3.4.* mdl.2.4.*";
            byte[] bChannel =channel.getBytes();

            //Redis用户认证
            String  token="mytoken";
            jedis.auth(token);

            //消息处理函数
            MessageHandler messageHandler = new MessageHandler();
            //订阅上交所Level1 股票数据
            jedis.subscribe(messageHandler, bChannel);
        }catch (Exception e){
            e.printStackTrace();
        }

    }
}

 class MessageHandler extends BinaryJedisPubSub{

     @Override
     //处理 Redis 消息
     public void onMessage(byte[] bChannel, byte[] body) {
         try{
             String channel = new String(bChannel);
             //反序列化 PB 格式消息
             if(channel.indexOf("mdl.3.4")>=0){
                 Method method = MDLSHL1Msg.Equity.class.getDeclaredMethod("parseFrom", byte[].class);
                 MDLSHL1Msg.Equity equity = (MDLSHL1Msg.Equity)method.invoke(null, body);
                 System.out.println(" SHL1.EQUITY " +
                                 " securityName=" + equity.getSecurityName() +
                                 " securityID=" + equity.getSecurityID() +
                                 " updateTime=" + equity.getUpdateTime() +
                                 " preCloPrice=" + equity.getPreCloPrice().getValue() +
                                 " highPrice=" + equity.getHighPrice().getValue() +
                                 " openPrice " + equity.getOpenPrice().getValue() +
                                 " lowPrice=" + equity.getLowPrice().getValue() +
                                 " lastPrice=" + equity.getLastPrice().getValue()
                 );
             }
			 else if (channel.indexOf("mdl.2.4")>=0) {
				System.out.println("heart beat");
			 }
         }catch(Exception e){
             e.printStackTrace();
         }
     }

 }