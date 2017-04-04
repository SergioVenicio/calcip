ip = input('IP: ').split('.')
mask = input('Mask: ').split('.')

if(len(ip) == 4 and len(mask) == 4):
    broadcast, ip_rede = [], []
    r, b, bin_rede, bin_broadcast, bin_ip = '', '', '', '', ''


    for i in range(len(ip)):
        ip_rede.append(int(ip[i]) & int(mask[i]))
        broadcast.append((~int(mask[i])&0xff) | int(ip_rede[i]))

    for i in range(len(ip_rede)):
        if(i <= 3):
            r += str(ip_rede[i]) + '.'
            b += str(broadcast[i]) + '.'
        else:
            r += str(ip_rede[i])
            b += str(broadcast[i])

        aux = ip_rede[i]
        binario = str(bin(int(aux)))
        bin_rede += binario[2:]

        aux = ip[i]
        binario = str(bin(int(aux)))
        bin_ip += binario[2:]

        aux = broadcast[i]
        binario = str(bin(int(aux)))
        bin_broadcast += binario[2:]



    ip = ".".join(ip)
    mask = '.'.join(mask)

    print('Rede {0}, Ip {1}, BroadCast {2}, Mascara {3}'.format(r, ip, b, mask))
    print('Binário da rede: {0}'.format(bin_rede))
    print('Binário do host: {0}'.format(bin_ip))
    print('Binário do brodcast: {0}'.format(bin_broadcast))

else:
    print('Ip e/ou mascara invalidos!')
