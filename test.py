from train import train_from_corpus
from classify import classify






if __name__=="__main__":
	spams = []
	hams = []
	add_files("corpus/easy_ham", hams)
	add_files("corpus/spam", spams)
	train_from_corpus(hams, "ham")
	train_from_corpus(spams, "spam")

	print classify("""
	
	From mail0206@btamail.net.cn  Mon Jun 24 17:08:42 2002
Return-Path: mail0206@btamail.net.cn
Delivery-Date: Thu May 30 22:48:40 2002
Received: from mandark.labs.netnoteinc.com ([213.105.180.140]) by
    dogma.slashnull.org (8.11.6/8.11.6) with ESMTP id g4ULmdO24956 for
    <jm@jmason.org>; Thu, 30 May 2002 22:48:40 +0100
Received: from app_server1.sysnet.com.cn ([211.101.210.170]) by
    mandark.labs.netnoteinc.com (8.11.2/8.11.2) with ESMTP id g4ULma709747 for
    <jm@netnoteinc.com>; Thu, 30 May 2002 22:48:37 +0100
Received: from smtp0452.mail.yahoo.com ([12.8.132.8]) by
    app_server1.sysnet.com.cn with Microsoft SMTPSVC(5.0.2195.2966);
    Fri, 31 May 2002 05:47:05 +0800
Date: Thu, 30 May 2002 14:47:51 -0700
From: "Bradford Jackson"<mail0206@btamail.net.cn>
X-Priority: 3
To: webtv@netnook.com
Subject: FREE Travel package and Business Kit...
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Message-Id: <APP_SERVER1LewpRnaF0000f061@app_server1.sysnet.com.cn>
X-Originalarrivaltime: 30 May 2002 21:47:05.0763 (UTC) FILETIME=[8A56FF30:01C20823]
X-Keywords: 
Content-Transfer-Encoding: 7bit

Hotels Etc. is giving away 10,000 of our $495 Travel Packages FREE, to help the USA in the promotion of the travel business. The first 10,000 customers who sign up will receive over $5000 worth of other free products.
 
This includes:
               
                FREE 50% off card/vouchers for all hotels in usa 
 
                FREE $2,000 Las Vegas, Hawaii & Orlando gift check 
 
                FREE vacation certificates for Las Vegas, Hawaii and Orlando 
    
As an added bonus you will receive the following:
     
   Free Kodak film for life coupon 
 
   FREE Vacation Certificate...
   Lodging for three exciting days and two fun-filled nights at your choice of one of 20 fabulous destinations including Las Vegas and Lake Tahoe, Nevada; Daytona    Beach, Florida; Cancun and  Puerto Vallarta, Mexico; Gatlinburg, Tennessee;Branson, Missouri;Honolulu, Hawaii; and many  more! ($175 Value) 
 
This also comes with a free home business where you work as much as you like, whenever you like, to make your own money with your own business.
 
Visit us at our website to see more info on all of these amazing oportunities.
Do not miss out.
 
Visit http://freetravel@66.46.145.35/members/travel/
""")
