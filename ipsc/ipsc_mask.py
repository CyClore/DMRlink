# Copyright (c) 2013 Cortney T. Buffington, N0MJS and the K0USY Group. n0mjs@me.com
#
# This work is licensed under the Creative Commons Attribution-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.

# LINKING STATUS:
#	Byte 1 - BIT FLAGS:
#	      xx.. .... = Peer Operational (01 only known valid value)
#	      ..xx .... = Peer MODE: 00 - No Radio, 01 - Analog, 10 - Digital
#	      .... xx.. = IPSC Slot 1: 10 on, 01 off 
#	      .... ..xx = IPSC Slot 2: 10 on, 01 off
#   MASK VALUES:
PEER_OP_MSK       = 0b01000000
PEER_MODE_MSK    = 0b00110000
PEER_MODE_ANALOG  = 0b00010000
PEER_MODE_DIGITAL = 0b00100000
IPSC_TS1_MSK      = 0b00001100
IPSC_TS2_MSK      = 0b00000011

#SERVICE FLAGS:

#	Byte 1 - 0x00  	= Unknown
#	Byte 2 - 0x00	= Unknown
#	Byte 3 - BIT FLAGS:
#	      x... .... = CSBK Message
#	      .x.. .... = Repeater Call Monitoring
#	      ..x. .... = 3rd Party "Console" Application
#	      ...x xxxx = Unknown - default to 0
#   MASK VALUES:
CSBK_MSK          = 0b10000000
RPT_MON_MSK       = 0b01000000
CON_APP_MSK       = 0b00100000

#	Byte 4 = BIT FLAGS:
#	      x... .... = XNL Connected (1=true)
#	      .x.. .... = XNL Master Device
#	      ..x. .... = XNL Slave Device
#	      ...x .... = Set if packets are authenticated
#	      .... x... = Set if data calls are supported
#	      .... .x.. = Set if voice calls are supported
#	      .... ..x. = Unknown - default to 0
#	      .... ...x = Set if master
#   MASK VALUES:
XNL_STAT_MSK       = 0b10000000
XNL_MSTR_MSK       = 0b01000000
XNL_SLAVE_MSK      = 0b00100000
PKT_AUTH_MSK       = 0b00010000
DATA_CALL_MSK      = 0b00001000
VOICE_CALL_MSK     = 0b00000100
MSTR_PEER_MSK      = 0b00000001

# TIMESLOT CALL & STATUS BYTE

#   Byte 17 of Group and Private Voice/Data Packets
#       ..x.. ....TS Value (0=TS1, 1=TS2)
#       .x... ....TS In Progress/End (0=In Progress, 1=End)
#       Possible values: 0x00=TS1, 0x20=TS2, 0x40=TS1 End, 0x60=TS2 End
#   MASK VALUE:
END_MSK             = 0b01000000
TS_CALL_MSK         = 0b00100000