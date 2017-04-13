#!/usr/bin/python3
# -*- coding: utf8 -*-

ip = input('IP: ').split('.')
mask = input('Mask: ').split('.')

if(len(ip) == 4 and len(mask) == 4):
    broadcast, ip_rede = [], []
    r, b, bin_rede, bin_broadcast, bin_ip = '', '', '', '', ''


    for i in range(len(ip)):
        ip_rede.append(int(ip[i]) & int(mask[i]))
        broadcast.append((~int(mask[i])&0xff) | int(ip_rede[i]))

    for i in range(len(ip_rede)):
        if(i <= 4):
            r += str(ip_rede[i]) + '.'
            b += str(broadcast[i]) + '.'

            # Rede
            aux = ip_rede[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:] + '.'
            bin_rede += binario

            # IP
            aux = ip[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:] + '.'
            bin_ip += binario

            # Broad
            aux = broadcast[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:] + '.'
            bin_broadcast += binario
        else:
            r += str(ip_rede[i])
            b += str(broadcast[i])

            # Rede
            aux = ip_rede[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:]
            bin_rede += binario

            # IP
            aux = ip[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:]
            bin_ip += binario

            # Broad
            aux = broadcast[i]
            binario = str(bin(int(aux)))
            if str(binario[2:]) == str(0b0):
                binario = '00000000.'
            else:
                binario = binario[2:]
            bin_broadcast += binario


    ip = ".".join(ip)
    mask = '.'.join(mask)

    print('Rede {0}, Ip {1}, BroadCast {2}, Mascara {3}'.format(r, ip, b, mask))
    print('Binário da rede: {0}'.format(bin_rede))
    print('Binário do host: {0}'.format(bin_ip))
    print('Binário do brodcast: {0}'.format(bin_broadcast))
else:
    print('Digite um IP e uma mascara correta')
