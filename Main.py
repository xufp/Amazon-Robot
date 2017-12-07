# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-31 20:58:46
# @Last modified by:   LC
# @Last Modified time: 2017-03-23 17:20:39
# @Email: liangchaowu5@gmail.com

import time
import os
from Robot import Robot
from get_proxy_and_user_information.GetProxy import is_valid
from record_product_information.VisitRecord import get_proxyips
from record_product_information.VisitRecord import delete_invalidIP

if __name__ == '__main__':
    # provide the informaion of the product on Amazon, including asin and words for searching
    asin = 'B074XDBCK3'
    #asin = 'B002NSMFOQ'
    brand = 'DREAMRY-Multifunctional-Rechargeable-Conferences-Conversation-Black'
    search_words = 'digital voice recorders'
    add_to_cart_probability = 0.7
    #get all proxy ips from db, then test ip from each to each, delte invalid ip from db
    result = get_proxyips()
    if result is None:
        os._exit()
    index = 0
    while True:
        ip = result[index][0]
        if ip is None:
            break
        if not is_valid('https://www.amazon.co.uk', ip):
            delete_invalidIP(ip)
        else:
            print ip
            robot = Robot(ip)
            ###############################################
            # sign in and browse
            ###############################################
            """
            robot.sign_in()
            # one item
            robot.search_keywords(search_words)
            robot.simulate_browsing(search_words, asin, add_to_cart_probability)
            # another item
            # ....
            """
            ###############################################
            # sign up
            ###############################################
            #normal sign up
            """
            user_info = robot.generate_sign_up_user(random_password=True)
            robot.sign_up(user_info)
            """

            # sign up
            user_info = robot.generate_sign_up_user(random_password=True)
            robot.sign_up(user_info)
            time.sleep(5)
            robot.search_keywords(search_words)
            robot.simulate_browsing(brand, search_words, asin, add_to_cart_probability)
            robot.exit_driver()
        index += 1