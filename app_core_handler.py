#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

logger = logging.getLogger()
from pyxxnet3 import public_server_callback
from pyxxnet3 import public_server_interface
from pyxxnet3.pyxxconstant import *


class APP_CORE_HANDLER(public_server_callback.ServerCallback):
    endpoint_ids = [i for i in range(1)]
    # worker = app_worker.AppWorker()
    python = "python"

    wssclients = {}
    dbcclient = None

    def __init__(self):
        pass

    @staticmethod
    def my_servername():
        return "tcp_echo_svr"

    # -----------------------------------
    @staticmethod
    def listenconfig_get(key=""):  # 10.10.2.143
        c = {"addresslist": [("0.0.0.0", 11101, 0)], "eventloop": "select", }
        return c[key]
        return ""
    @staticmethod
    def connectconfig_get(key=""):
        server_addr_list = [("127.0.0.1", 11101, i) for i in APP_CORE_HANDLER.endpoint_ids]
        c = {"addresslist": server_addr_list, "eventloop": "select", }
        #return c[key]
        return ""

    @staticmethod
    def workerconfig_get(key=""):
        c = {"workercount": 0, }
        return c[key]

    @staticmethod
    def session_unpack_frombuffer(session, buffer):
        return (len(buffer), 0)

    @staticmethod
    def endpoint_unpack_frombuffer(endpoint, buffer):
        return APP_CORE_HANDLER.session_unpack_frombuffer(endpoint, buffer)

    @staticmethod
    def session_dispatch_packet(session, packet_cmd, packet_data):
        print("session>>{0}".format(packet_data))
        session.send(packet_data)

    @staticmethod
    def session_keeplive(session, status=0):
        if status == LIVE_STATUS.LIVE_STATUS_BEGIN:
            print("-----------session begin,welcome ..,say hello ")
            session.send("hello")
            return
        if status == LIVE_STATUS.LIVE_STATUS_KEEPLIVE:
            return
        if status == LIVE_STATUS.LIVE_STATUS_END:
            return

    @staticmethod
    def endpoint_dispatch_packet(endpoint, packet_cmd, packet_data):
        print("endpoint>>{0}".format(packet_data))

    @staticmethod
    def endpoint_keeplive(endpoint, status=0):
        return
        # print("keeplive",status)
        if status == LIVE_STATUS.LIVE_STATUS_BEGIN:
            endpoint.send("begin")
            APP_CORE_HANDLER.dbcclient = endpoint
            return
        if status == LIVE_STATUS.LIVE_STATUS_KEEPLIVE:
            endpoint.send("live")
            return
        if status == LIVE_STATUS.LIVE_STATUS_END:
            return
