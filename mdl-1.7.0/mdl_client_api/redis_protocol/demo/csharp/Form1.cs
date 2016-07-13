using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using datayes.mdl.mdl_szl1_pbmsg;
using datayes.mdl.mdl_shl1_pbmsg; 

namespace WindowsFormsApplication1
{
    class myobserver : IObserver<Sider.Message<byte[]>>
    {
        public void OnCompleted()
        {
        }
        public void OnError(System.Exception error)
        {
        }
        public void OnNext(Sider.Message<byte[]> msg)
        {
            if (msg.Type == Sider.MessageType.Message)
            {
                if (msg.SourceChannel.IndexOf("mdl.5.1") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_szl1_pbmsg.SZL1Index pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_szl1_pbmsg.SZL1Index>(stream);
                    Console.WriteLine(pbmsg.IndexName + " LastIndex:" + (float)(pbmsg.LastIndex.Value / (float)pbmsg.LastIndex.DecimalShift));
                }
                if (msg.SourceChannel.IndexOf("mdl.5.2") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_szl1_pbmsg.SZL1Stock pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_szl1_pbmsg.SZL1Stock>(stream);
                    Console.WriteLine(pbmsg.SecurityName + " LastIndex:" + (float)(pbmsg.LastPrice.Value / (float)pbmsg.LastPrice.DecimalShift));
                }   
                else if (msg.SourceChannel.IndexOf("mdl.3.4") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_shl1_pbmsg.Equity pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_shl1_pbmsg.Equity>(stream);
                    Console.WriteLine(pbmsg.SecurityName + " LastPrice:" + (float)(pbmsg.LastPrice.Value / (float)pbmsg.LastPrice.DecimalShift));
                    for (int i = 0; i < pbmsg.BidPriceLevel.Count; ++i)
                    {
                        Console.WriteLine("bid" + i + ": price=" + (float)(pbmsg.BidPriceLevel[i].Price.Value / (float)pbmsg.BidPriceLevel[i].Price.DecimalShift)
                            + "volume=" + pbmsg.BidPriceLevel[i].Volume);
                    }
                }
                else if (msg.SourceChannel.IndexOf("mdl.3.5") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_shl1_pbmsg.Funds pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_shl1_pbmsg.Funds>(stream);
                    Console.WriteLine(pbmsg.SecurityName + " LastPrice:" + (float)(pbmsg.LastPrice.Value / (float)pbmsg.LastPrice.DecimalShift));
                }
                else if (msg.SourceChannel.IndexOf("mdl.3.6") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_shl1_pbmsg.Bonds pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_shl1_pbmsg.Bonds>(stream);
                    Console.WriteLine(pbmsg.SecurityName + " LastPrice:" + (float)(pbmsg.LastPrice.Value / (float)pbmsg.LastPrice.DecimalShift));
                }
                else if (msg.SourceChannel.IndexOf("mdl.3.3") == 0)
                {
                    System.IO.MemoryStream stream = new System.IO.MemoryStream(msg.Body);
                    datayes.mdl.mdl_shl1_pbmsg.Indexes pbmsg = global::ProtoBuf.Serializer.Deserialize<datayes.mdl.mdl_shl1_pbmsg.Indexes>(stream);
                    Console.WriteLine(pbmsg.IndexName + " LastIndex:" + (float)(pbmsg.LastIndex.Value / (float)pbmsg.LastIndex.DecimalShift));
                }

            }
        }
    }
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Sider.RedisClient<byte[]> client = new Sider.RedisClient<byte[]>("127.0.0.1", 9379);

            if (!client.Auth("nopassword"))
            {
                Console.WriteLine("auth failed");
                return;
            }
            Console.WriteLine("auth ok"); 

            string[] keys = new string[6];
            keys[0] = "mdl.5.1.*";
            keys[1] = "mdl.5.2.*";
            keys[2] = "mdl.3.3.*";
            keys[3] = "mdl.3.4.*";
            keys[4] = "mdl.3.5.*";
            keys[5] = "mdl.3.6.*";
            IObservable<Sider.Message<byte[]>> ret = client.Subscribe(keys);
            ret.Subscribe(new myobserver());

            Console.WriteLine("receving message...");            
        }
    }
}
