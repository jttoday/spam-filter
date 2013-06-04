from classify import classify

simple_spam = """
	
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
"""

simple_ham = """
From martin@srv0.ems.ed.ac.uk  Wed Aug 28 10:55:21 2002
Return-Path: <martin@srv0.ems.ed.ac.uk>
Delivered-To: zzzz@localhost.netnoteinc.com
Received: from localhost (localhost [127.0.0.1])
	by phobos.labs.netnoteinc.com (Postfix) with ESMTP id 9AB2F43F9B
	for <zzzz@localhost>; Wed, 28 Aug 2002 05:55:20 -0400 (EDT)
Received: from phobos [127.0.0.1]
	by localhost with IMAP (fetchmail-5.9.0)
	for zzzz@localhost (single-drop); Wed, 28 Aug 2002 10:55:20 +0100 (IST)
Received: from n19.grp.scd.yahoo.com (n19.grp.scd.yahoo.com
    [66.218.66.74]) by dogma.slashnull.org (8.11.6/8.11.6) with SMTP id
    g7S8q0Z16982 for <zzzz@example.com>; Wed, 28 Aug 2002 09:52:00 +0100
X-Egroups-Return: sentto-2242572-53138-1030524726-zzzz=example.com@returns.groups.yahoo.com
Received: from [66.218.67.199] by n19.grp.scd.yahoo.com with NNFMP;
    28 Aug 2002 08:52:06 -0000
X-Sender: martin@srv0.ems.ed.ac.uk
X-Apparently-To: zzzzteana@yahoogroups.com
Received: (EGP: mail-8_1_0_1); 28 Aug 2002 08:52:06 -0000
Received: (qmail 18008 invoked from network); 28 Aug 2002 08:52:06 -0000
Received: from unknown (66.218.66.216) by m6.grp.scd.yahoo.com with QMQP;
    28 Aug 2002 08:52:06 -0000
Received: from unknown (HELO haymarket.ed.ac.uk) (129.215.128.53) by
    mta1.grp.scd.yahoo.com with SMTP; 28 Aug 2002 08:52:05 -0000
Received: from srv0.ems.ed.ac.uk (srv0.ems.ed.ac.uk [129.215.117.0]) by
    haymarket.ed.ac.uk (8.11.6/8.11.6) with ESMTP id g7S8q4311684 for
    <forteana@yahoogroups.com>; Wed, 28 Aug 2002 09:52:04 +0100 (BST)
Received: from EMS-SRV0/SpoolDir by srv0.ems.ed.ac.uk (Mercury 1.44);
    28 Aug 02 09:52:04 +0000
Received: from SpoolDir by EMS-SRV0 (Mercury 1.44); 28 Aug 02 09:51:51 +0000
Organization: Management School
To: zzzzteana@yahoogroups.com
Message-Id: <3D6C9D54.27778.240F6D50@localhost>
Priority: normal
In-Reply-To: <E17jyHY-0004Ja-00@gadolinium.btinternet.com>
X-Mailer: Pegasus Mail for Windows (v4.01)
Content-Description: Mail message body
From: "Martin Adamson" <martin@srv0.ems.ed.ac.uk>
MIME-Version: 1.0
Mailing-List: list zzzzteana@yahoogroups.com; contact
    forteana-owner@yahoogroups.com
Delivered-To: mailing list zzzzteana@yahoogroups.com
Precedence: bulk
List-Unsubscribe: <mailto:zzzzteana-unsubscribe@yahoogroups.com>
Date: Wed, 28 Aug 2002 09:51:47 +0100
Subject: Re: [zzzzteana] That wacky imam
Reply-To: zzzzteana@yahoogroups.com
Content-Type: text/plain; charset=US-ASCII
Content-Transfer-Encoding: 7bit


> Sheikh Abu Hamza al-Masri, our maddest of mad mullahs and a cartoon bogeyman
> to scare the kiddies, spent a quiet and contemplative bank holiday playing
> with his own children in Victoria Park, Hackney.

For an alternative, and rather more factually based, rundown on Hamza's 
career, including his belief that all non Muslims in Yemen should be murdered 
outright:

http://memri.org/bin/articles.cgi?Page=archives&Area=ia&ID=IA7201

Martin


------------------------ Yahoo! Groups Sponsor ---------------------~-->
4 DVDs Free +s&p Join Now
http://us.click.yahoo.com/pt6YBB/NXiEAA/MVfIAA/7gSolB/TM
---------------------------------------------------------------------~->

To unsubscribe from this group, send an email to:
forteana-unsubscribe@egroups.com

 

Your use of Yahoo! Groups is subject to http://docs.yahoo.com/info/terms/ 
"""




if __name__=="__main__":
	print classify(simple_spam)
	print classify(simple_ham)


