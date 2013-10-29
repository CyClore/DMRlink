# Copyright (c) 2013 Cortney T. Buffington, N0MJS and the K0USY Group. n0mjs@me.com
#
# This work is licensed under the Creative Commons Attribution-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.

from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet import task

import binascii
import dmrlink
from dmrlink import IPSC, UnauthIPSC, NETWORK, networks, get_info

class bridgeIPSC(IPSC):
    
    def __init__(self, *args, **kwargs):
        IPSC.__init__(self, *args, **kwargs)
        self.ACTIVE_CALLS = []
        
    def datagramReceived(self, data, (host, port)):
        print(binascii.b2a_hex(data))
        
        
    #************************************************
    #     CALLBACK FUNCTIONS FOR USER PACKET TYPES
    #************************************************

    def call_ctl_1(self, _network, _data):
        pass
    
    def call_ctl_2(self, _network, _data):
        pass
    
    def call_ctl_3(self, _network, _data):
        pass
    
    def xcmp_xnl(self, _network, _data):
        pass
    
    def group_voice(self, _network, _src_sub, _dst_sub, _ts, _end, _peerid, _data):
        for source in NETWORK[_network]['RULES']['GROUP_VOICE']:
            # Matching for rules is against the Destination Group in the SOURCE packet (SRC_GROUP)
            if source['SRC_GROUP'] == _src_group:
                _target = source['DST_NET']
                _target_sock = NETWORK[_target]['MASTER']['IP'], NETWORK[_target]['MASTER']['PORT']
                # Re-Write the IPSC SRC to match the target network's ID
                _data = _data.replace(_peerid, NETWORK[_target]['LOCAL']['RADIO_ID'])
                # Re-Write the destinaion Group ID
                _data = _data.replace(_src_group, source['DST_GROUP'])
                # Calculate and append the authentication hash for the target network... if necessary
                if NETWORK[_target]['LOCAL']['AUTH_KEY'] == True:
                    _data = hashed_packet(NETWORK[_target]['LOCAL']['AUTH_KEY'], _data)
                # Send the packet to all peers in the target IPSC
                send_to_ipsc(_target, _data)
    
    def private_voice(self, _network, _src_sub, _dst_sub, _ts, _end, _peerid, _data): 
        pass
    
    def group_data(self, _network, _src_sub, _dst_sub, _ts, _end, _peerid, _data):    
        pass
    
    def private_data(self, _network, _src_sub, _dst_sub, _ts, _end, _peerid, _data):    
        pass

        
for ipsc_network in NETWORK:
    if (NETWORK[ipsc_network]['LOCAL']['ENABLED']):
        if NETWORK[ipsc_network]['LOCAL']['AUTH_ENABLED'] == True:
            networks[ipsc_network] = bridgeIPSC(ipsc_network)
        else:
            networks[ipsc_network] = UnauthIPSC(ipsc_network)
        reactor.listenUDP(NETWORK[ipsc_network]['LOCAL']['PORT'], networks[ipsc_network])
reactor.run()