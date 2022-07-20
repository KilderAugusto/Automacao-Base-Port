import time, datetime
from datetime import datetime
import os, platform
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
import json


class selenium:
    # =============================
    # Chrome Driver Reference
    # https://chromedriver.chromium.org/downloads
    #
    # Selenium Reference
    # https://selenium-python.readthedocs.io/getting-started.html
    #
    # =============================
    global saida
    saida = {
        'Status Base Port': {
            'Estado da Rede Wi-Fi': {
                'Status': {},
                'Estado do Repetidor': {},
            },
            'Associado a rede wifi': {
                'SSID': {},
                'Canal': {},
                'RSSI': {},
                'Tipo de Segurança': {},
                'Modo Repetidor Status Wi-Fi 5GHz': {},
            },

            'Estado da Rede Wifi': {
                'status': {},

            },
            'Nome': {
                'Nome do Wi-Fi': {},

            },
            'Ocultar Rede Wi-Fi': {
                'Sim ou Não': {},
            },

            'Nível': {
                'Nível de Segurança': {}
            },

            'Senha': {
                'Senha Wi-Fi': {},
            },

            'Criptografia': {
                'Tipo de Criptografia': {},
            },
            'Status de Encriptação': {
                'Encriptação': {},
            },
            'Canal': {
                'Número de canal wifi': {},
                'Canal atual': {},
            },
            'Roaming Wi-Fi': {
                'Status de Roaming': {},
                'Função Roaming': {},
                'Configure Automaticamente': {},
            },
            'Informações do dispositivo': {
                'Nome do Dispositivo': {},
                'Modelo': {},
                'Número de série': {},
                'Versão de Hardware': {},
                'Versão de Software': {},
                'Versão de Firmware': {},
                'Código do país': {},
                'Status': {},
                'Função Roaming': {},
            },

            'Informações Wifi-Fi 5GHz': {
                'Status Wi-Fi': {},
                'Nome da rede (SSID)': {},
                'Modo': {},
                'Esconder SSID': {},
                'Autenticação': {},
                'Encriptação': {},
                'Canal Atual': {},
             },
            'Informações da LAN': {
              'Endereço IP': {},
              'Máscara de Rede': {},
              'Gateway': {},
              'DHCP': {},
            },

            'Informações Wi-Fi': {
               'Status Wi-Fi': {},
               'Nome da rede (SSID)': {},
               'Esconder SSID': {},
               'Autenticação': {},
               'Encriptação': {},
               'Canal Atual': {},
            },


            'Rede Local': {
                'DHCP': {},
                'Endereço IP': {},
                'Máscara de Subrede': {},
                'Gateway Padrão': {},
                'DNS': {},
            },
            'Configuração Avançada': {
                'Wifi5': {
                    'SSID0': {},
                    'SSID1': {},
                    'SSID2': {},
                    'SSID3': {},
                },
                'Wifi2': {
                    'SSID': {},
                    'SSID1': {},
                    'SSID2': {},
                    'SSID3': {},

                }
            }
        }
    }


    def verifyOs(self):
        global OperationalSystem, driver
        OperationalSystem = platform.system()
        if OperationalSystem == 'Windows':
            PATH = 'Setup/chromedriver_win32/chromedriver.exe'
        else:
            PATH = 'Setup/chromedriver_linux64/chromedriver'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print(' -- Seu Sistema Operacional é: ', OperationalSystem)

    def acessoWebBasePort(self, ip, senha):
        # Acessar URL
        driver.maximize_window()
        driver.get('http://192.168.15.190/')  # Pagina de acesso ao Roteador
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[3]/div/div[2]/div[1]/div/input').send_keys(senha)
        driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[3]/div/div[2]/div[2]/button').click()
        # Login completo

    def atualizacaoFw(self):
        versao_frw_desejada = 'GL_g8.1_RG3110W0.6.1'
        sleep(1)
        driver.find_element(by=By.ID, value='divMenu').click()
        time.sleep(1)
        driver.find_element(by=By.CLASS_NAME, value='cMnuDeviceInfo').click()
        sleep(1)
        versao_firmware = driver.find_element(by=By.ID, value='spnFw').text
        sleep(1)
        #print(type(versao_firmware))
        print('⌛ Analisando versão de Firmware ⌛')
        print(f'Firmware em Produção ↪ \033[4;36m', versao_firmware, '\033[m ↩')
        #atualizacao_Fw = 'GL_g8.1_RG3110W0.6.1.'
        if versao_firmware != versao_frw_desejada:
            sleep(3)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/span[2]').click()
            sleep(2)
            driver.find_element(by=By.CLASS_NAME, value='cMnuFwUpgrade').click()
            sleep(3)
            driver.find_element(by=By.ID, value='btnFile').send_keys("C://Users/40414300/Downloads/atualizacao-FW/GL_g8.1_RG3110W0.6.1.img")
            time.sleep(3)
            driver.find_element(by=By.ID, value='btnFwApply1').click()
            driver.implicitly_wait(10)
            time.sleep(250)
        else:
            print('🔄SEM VERSÃO DE FIRMWARE PARA ATUALIZAÇÃO🔄')





    def acessoWebBasePort(self, ip, senha):
        # Acessar URL
        driver.maximize_window()
        driver.get('http://192.168.15.190/')  # Pagina de acesso ao Roteador
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[3]/div/div[2]/div[1]/div/input').send_keys(senha)
        driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[3]/div/div[2]/div[2]/button').click()
        # Login completo


    def capturaWifi5Ghz(self):
        wifi5GHz = driver.find_element(by=By.XPATH,
                                       value='//html/body/div[9]/div[2]/div[4]/div[1]/div[2]/input').is_selected()
        #print(wifi5GHz)
        if wifi5GHz == True:
            list = ['Ativo']
            saida['Status Base Port']['Estado da Rede Wi-Fi']['Status'] = list[0]
        else:
            list = ['Inativo']
            saida['Status Base Port']['Estado da Rede Wi-Fi']['Status'] = list[0]

        time.sleep(2)
        # tratando ERROr caso a basep port seja automatizada via cabo ETH
        try:
            nome_wifi = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[9]/div[2]/div[4]/div[2]/div[2]/input').get_attribute(
                "value")
            list = nome_wifi.split('\n')
            #print(list)

            ocultarWifi = driver.find_element(by=By.XPATH,
                                              value='/html/body/div[9]/div[2]/div[4]/div[3]/div[2]/input').is_selected()
            #print(ocultarWifi)
            if ocultarWifi == True:
                list = ['Sim']
                saida['Status Base Port']['Ocultar nome da rede Wi-Fi']['Sim ou Nao'] = list[0]
            else:
                list = ['Nao']
                saida['Status Base Port']['Ocultar nome da rede Wi-Fi']['Sim ou Nao'] = list[0]
                print(json.dumps(saida['Status Base Port']['Ocultar nome da rede Wi-Fi']))


        except Exception:
            print('▓' * 35)
            print('▓▓AUTOMATIZANDO INTERFACE GRÁFICA▓▓')
            print('▓' * 35)

        time.sleep(3)

        try:
            senhawifi5 = driver.find_element(by=By.XPATH,
                                             value='/html/body/div[9]/div[2]/div[4]/div[4]/div[2]/div/input').get_attribute("value")
            div_senha = senhawifi5.split('\n')
            #print(div_senha)
            saida['Status Base Port']['senha']['Senha Wifi5'] = div_senha[0]
            print(json.dumps(saida['Status Base Port']['senha']))
            sleep(3)


        except Exception:
            print('CARREGANDO ▪▫▪▫▪▫')

        try:
            # capture level wifi5
            nivel = driver.find_element(by=By.XPATH,
                                        value='/html/body/div[9]/div[2]/div[4]/div[5]/div[2]/div/span').text
            div_nivel = nivel.split('\n')
            #print(div_nivel)
            saida['Status Base Port']['Nivel de Seguranca da Senha']['Nivel'] = div_nivel[1]
            print(json.dumps(saida['Status Base Port']['Nivel de Seguranca da Senha']))
        except Exception:
            time.sleep(5)
            print('OBTENDO INFORMAÇÕES ▪▫▪▫▪▫▪▫▪▫')
        try:
            # capture type cryptography
            tipo_criptografia = driver.find_element(by=By.ID, value='selAuth5g')
            select_object = Select(tipo_criptografia)
            valor_selecionado = select_object.first_selected_option.text
            lista = valor_selecionado.split('\n')
            print(list)
            saida['Status Base Port']['Criptografia']['Tipo de Criptografia'] = lista[0].strip()
            print(json.dumps(saida['Status Base Port']['Criptografia']))

            # encryption
            encriptacao = driver.find_element(by=By.ID, value='selEnc5g')
            select_object = Select(encriptacao)
            value_selected = select_object.first_selected_option.text
            div = value_selected.split('\n')
            print(div)
            saida['Status Base Port']['Status de Encriptação']['Encriptação'] = div[0].strip()
            print(json.dumps(saida['Status Base Port']['Status de Encriptação']))

            # number channel
            numero_canal = driver.find_element(by=By.ID, value='selCh5g')
            select_object = Select(numero_canal)
            value_select = select_object.first_selected_option.text
            div = value_select.split('\n')
            print(div)
            saida['Status Base Port']['Canal']['Número de canal wifi'] = div[0]
            print(json.dumps(saida['Status Base Port']['Canal']))

            # current channel
            canal_atual = driver.find_element(by=By.ID, value='spnChCurr5g').text
            list = canal_atual.split('\n')
            print(list)
            saida['Status Base Port']['Canal']['Canal atual'] = list[0]
            print(json.dumps(saida['Status Base Port']['Canal']))
        except Exception:
            time.sleep(5)
            print('CAPTURANDO DADOS ▪▫▪▫▪▫▪▫▪▫▫▪▫▪▫▪▫')
            time.sleep(3)

        try:
            # estado do repetidor
            estado_repetidor = driver.find_element(by=By.XPATH,
                                                   value='/html/body/div[9]/div[2]/div[4]/div[2]/div[2]').text
            list = estado_repetidor.split('\n')
            print(list)
            saida['Status Base Port']['Estado da Rede Wi-Fi']['Estado do Repetidor'] = list[0]
            print(json.dumps(saida['Status Base Port']['Estado da Rede Wi-Fi']))
            # Associado a rede wi-fi
            driver.implicitly_wait(5)
            sleep(7)
            associado_wifi = driver.find_element(by=By.XPATH,
                                                 value='/html/body/div[9]/div[2]/div[4]/div[3]/div[1]/div[2]').text
            div = associado_wifi.split()
            print(div)
            saida['Status Base Port']['Associado a rede wifi']['SSID'] = div[6]
            sleep(5)
            saida['Status Base Port']['Associado a rede wifi']['Canal'] = div[7]
            sleep(5)
            saida['Status Base Port']['Associado a rede wifi']['RSSI'] = div[8]
            sleep(5)
            saida['Status Base Port']['Associado a rede wifi']['Tipo de Segurança'] = div[9]
            print(json.dumps(saida['Status Base Port']['Associado a rede wifi']))
            sleep(5)
            modo_repetidor = driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[2]/div[4]/div[4]').text
            div = modo_repetidor.split('\n')
            print(div)
            saida['Status Base Port']['Associado a rede wifi']['Modo Repetidor Status Wi-Fi 5GHz'] = div[1]
            print(json.dumps(saida['Status Base Port']['Associado a rede wifi']))

        except Exception:
            print('CAPTURANDO DADOS..................')

    def capturaWifi(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[3]/a').click()
        sleep(2)
        wifi = driver.find_element(by=By.XPATH,
                                   value='/html/body/div[9]/div[2]/div[4]/div[1]/div[2]/input').is_selected()
        print(wifi)
        # print(wifi2)
        if wifi == True:
            list = ['Ativo']
            saida['Status Base Port']['Estado da Rede Wifi']['status'] = list[0]
        else:
            list = ['Inativo']
            saida['Status Base Port']['Estado da Rede Wifi']['status'] = list[0]
        # print(json.dumps(saida['Status Base Port']['Estado da Rede Wifi']))
        time.sleep(2)
        nome_wifi = driver.find_element(by=By.XPATH,
                                        value='/html/body/div[9]/div[2]/div[4]/div[2]/div[2]/input').get_attribute(
            "value")
        div = nome_wifi.split('\n')
        # print(div)
        saida['Status Base Port']['Nome']['Nome do Wi-Fi'] = div[0]
        print(json.dumps(saida['Status Base Port']['Nome']))
        sleep(3)
        ocultar_nome = driver.find_element(by=By.XPATH,
                                           value='/html/body/div[9]/div[2]/div[4]/div[3]/div[2]/input').is_selected()
        print(div)
        if ocultar_nome == True:
            list = ['Sim']
            saida['Status Base Port']['Ocultar Wi-Fi']['Sim ou Não'] = list[0]
        else:
            list = ['Não']
            saida['Status Base Port']['Ocultar Rede Wi-Fi']['Sim ou Não'] = list[0]
        print(json.dumps(saida['Status Base Port']['Ocultar Rede Wi-Fi']))
        sleep(2)

        # capture password wifi
        senha_wifi = driver.find_element(by=By.XPATH,
                                         value='/html/body/div[9]/div[2]/div[4]/div[4]/div[2]/div/input').get_attribute(
            "value")
        list = senha_wifi.split('\n')
        # print(div)
        saida['Status Base Port']['Senha']['Senha Wi-Fi'] = list[0]
        print(json.dumps(saida['Status Base Port']['Senha']))
        sleep(3)

        # capture level security
        nivel_seguranca = driver.find_element(by=By.XPATH,
                                              value='/html/body/div[9]/div[2]/div[4]/div[5]/div[2]/div').text
        list1 = nivel_seguranca.split('\n')
        # print(div)
        saida['Status Base Port']['Nível']['Nível de Segurança'] = list1[0]
        print(json.dumps(saida['Status Base Port']['Nível']))

        # capture type cryptography
        tipo_criptografia = driver.find_element(by=By.ID, value='selAuth2g')
        select_object = Select(tipo_criptografia)
        valor_selecionado = select_object.first_selected_option.text
        lista = valor_selecionado.split('\n')
        print(list)
        saida['Status Base Port']['Criptografia']['Tipo de Criptografia'] = lista[0].strip()
        print(json.dumps(saida['Status Base Port']['Criptografia']))

        # encryption
        encriptacao = driver.find_element(by=By.ID, value='selEnc2g')
        select_object = Select(encriptacao)
        value_selected = select_object.first_selected_option.text
        div = value_selected.split('\n')
        print(div)
        saida['Status Base Port']['Status de Encriptação']['Encriptação'] = div[0].strip()
        print(json.dumps(saida['Status Base Port']['Status de Encriptação']))

        # number channel
        numero_canal = driver.find_element(by=By.ID, value='selCh2g')
        select_object = Select(numero_canal)
        value_select = select_object.first_selected_option.text
        div = value_select.split('\n')
        print(div)
        saida['Status Base Port']['Canal']['Número de canal wifi'] = div[0]
        print(json.dumps(saida['Status Base Port']['Canal']))

        # current channel
        canal_atual = driver.find_element(by=By.ID, value='spnChCurr2g').text
        list = canal_atual.split('\n')
        print(list)
        saida['Status Base Port']['Canal']['Canal atual'] = list[0]
        print(json.dumps(saida['Status Base Port']['Canal']))

    def capturaRoaming(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[5]/a').click()
        sleep(3)
        # capture Roaming
        status_roaming = driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[2]/div[3]').text
        div = status_roaming.split('\n')
        print(div)
        saida['Status Base Port']['Roaming Wi-Fi']['Status de Roaming'] = div[1]
        saida['Status Base Port']['Roaming Wi-Fi']['Função Roaming'] = div[3]
        print(json.dumps(saida['Status Base Port']['Roaming Wi-Fi']))

        config_automatic = driver.find_element(by=By.XPATH,
                                               value='/html/body/div[9]/div[2]/div[7]/div/label/select').is_enabled()
        print(config_automatic)
        if config_automatic == True:
            list = ['Ativo']
            saida['Status Base Port']['Roaming Wi-Fi']['Configure Automaticamente'] = list[0].strip()
        else:
            list = ['Inativo']
            saida['Status Base Port']['Roaming Wi-Fi']['Configure Automaticamente'] = list[0].strip()
        print(json.dumps(saida['Status Base Port']['Roaming Wi-Fi']))

    def capturaInfoDispositivos(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[9]/a').click()
        sleep(3)

        #Informações do dispositivo
        nome_dispositivo = driver.find_element(by=By.ID, value='spnName').text
        div = nome_dispositivo.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Nome do Dispositivo'] = div[0]

        modelo = driver.find_element(by=By.ID, value='spnModel').text
        div = modelo.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Modelo'] = div[0]

        numero_serie = driver.find_element(by=By.ID, value='spnSn').text
        div = numero_serie.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Número de série'] = div[0]

        versao_hardware = driver.find_element(by=By.ID, value='spnHw').text
        div = versao_hardware.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Versão de Hardware'] = div[0]

        versao_software = driver.find_element(by=By.ID, value='spnSw').text
        div = versao_software.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Versão de Software'] = div[0]

        versao_firmware = driver.find_element(by=By.ID, value='spnFw').text
        div = versao_firmware.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Versão de Firmware'] = div[0]

        codigo_pais = driver.find_element(by=By.ID, value='spnCc').text
        div = codigo_pais.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Código do país'] = div[0]
        sleep(2)
        status = driver.find_element(by=By.ID, value='spnState').text
        div = status.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Status'] = div[0]
        sleep(2)
        funcao_roaming = driver.find_element(by=By.ID, value='spnRoam').text
        div = funcao_roaming.split('\n')
        print(div)
        saida['Status Base Port']['Informações do dispositivo']['Função Roaming'] = div[0]
        sleep(2)

        # info wifi5ghz
        status_wifi = driver.find_element(by=By.ID, value='spnEn5g').text
        div = status_wifi.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Status Wi-Fi'] = div[0]

        nome_rede = driver.find_element(by=By.ID, value='spnSsid5g').text
        div = nome_rede.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Nome da rede (SSID)'] = div[0]

        modo = driver.find_element(by=By.ID, value='spnMode5g').text
        div = modo.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Modo'] = div[0]

        esconder_ssid = driver.find_element(by=By.ID, value='spnHide5g').text
        div = esconder_ssid.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Esconder SSID'] = div[0]

        autenticacao = driver.find_element(by=By.ID, value='spnAuth5g').text
        div = autenticacao.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Autenticação'] = div[0]

        encriptacao = driver.find_element(by=By.ID, value='spnEnc5g').text
        div = encriptacao.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Encriptação'] = div[0]

        canal_atual = driver.find_element(by=By.ID, value='spnCh5g').text
        div = canal_atual.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wifi-Fi 5GHz']['Canal Atual'] = div[0]



        time.sleep(3)


        # info Lan
        endereco_ip = driver.find_element(by=By.ID, value='spnIpAddr').text
        div = endereco_ip.split('\n')
        print(div)
        saida['Status Base Port']['Informações da LAN']['Endereço IP'] = div[0]

        mascara_rede = driver.find_element(by=By.ID, value='spnMask').text
        div = mascara_rede.split('\n')
        print(div)
        saida['Status Base Port']['Informações da LAN']['Máscara de Rede'] = div[0]

        gateway = driver.find_element(by=By.ID, value='spnGate').text
        div = gateway.split('\n')
        print(div)
        saida['Status Base Port']['Informações da LAN']['Gateway'] = div[0]

        dhcp = driver.find_element(by=By.ID, value='spnDhcpc').text
        div = dhcp.split('\n')
        print(div)
        saida['Status Base Port']['Informações da LAN']['DHCP'] = div[0]

        time.sleep(3)

        # info wifi

        status_wifi = driver.find_element(by=By.ID, value='spnEn2g').text
        div = status_wifi.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Status Wi-Fi'] = div[0]

        nome_rede = driver.find_element(by=By.ID, value='spnSsid2g').text
        div = nome_rede.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Nome da rede (SSID)'] = div[0]

        esconder_ssid2 = driver.find_element(by=By.ID, value='spnHide2g').text
        div = esconder_ssid2.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Esconder SSID'] = div[0]

        autenticacao2 = driver.find_element(by=By.ID, value='spnAuth2g').text
        div = autenticacao2.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Autenticação'] = div[0]

        encriptacao2 = driver.find_element(by=By.ID, value='spnEnc2g').text
        div = encriptacao2.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Encriptação'] = div[0]

        canal_atual2 = driver.find_element(by=By.ID, value='spnCh2g').text
        div = canal_atual2.split('\n')
        print(div)
        saida['Status Base Port']['Informações Wi-Fi']['Canal Atual'] = div[0]



    def capturaRedeLocal(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[11]/a').click()
        sleep(3)
        dhcp = driver.find_element(by=By.XPATH, value='/html/body/div[9]/div[2]/div[3]/div[1]').is_enabled()
        print(dhcp)
        if dhcp == True:
            list = ['Ativo']
            saida['Status Base Port']['Rede Local']['DHCP'] = list[0]
        elif dhcp == False:
            list2 = ['Inativo']
            saida['Status Base Port']['Rede Local']['DHCP'] = list2[0]
        sleep(3)
        # capture end: IP
        end_IP = driver.find_element(by=By.ID, value='txtAddr').get_attribute("value")
        div = end_IP.split()
        # print(div)
        saida['Status Base Port']['Rede Local']['Endereço IP'] = div[0]

        # capture mask sub
        mask_subrede = driver.find_element(by=By.ID, value='txtMask').get_attribute("value")
        div = mask_subrede.split()
        # print(div)
        saida['Status Base Port']['Rede Local']['Máscara de Subrede'] = div[0]

        # capture Gateway
        gateway_padrao = driver.find_element(by=By.ID, value='txtGate').get_attribute("value")
        div = gateway_padrao.split()
        # print(div)
        saida['Status Base Port']['Rede Local']['Gateway Padrão'] = div[0]

        # capture DNS
        dns = driver.find_element(by=By.ID, value='txtDns').get_attribute("value")
        div = dns.split()
        # print(div)
        saida['Status Base Port']['Rede Local']['DNS'] = div[0]
        driver.implicitly_wait(3)

    def capturaAvancada(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[15]/a').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[15]/ul/li[1]/a').click()
        sleep(10)

        ssid0 = driver.find_element(by=By.ID, value='txtSsid_0').get_attribute("value")
        list_ssid0 = ssid0.split('\n')
        print(list_ssid0)
        sleep(3)
        ssid1 = driver.find_element(by=By.ID, value='txtSsid_1').get_attribute("value")
        list_ssid1 = ssid1.split('\n')
        # print(list_ssid1)
        sleep(3)
        ssid2 = driver.find_element(by=By.ID, value='txtSsid_2').get_attribute("value")
        list_ssid2 = ssid2.split('\n')
        # print(list_ssid2)
        sleep(3)
        ssid3 = driver.find_element(by=By.ID, value='txtSsid_3').get_attribute("value")
        list_ssid3 = ssid3.split('\n')
        sleep(3)
        saida['Status Base Port']['Configuração Avançada']['Wifi5']['SSID0'] = list_ssid0[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi5']['SSID1'] = list_ssid1[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi5']['SSID2'] = list_ssid2[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi5']['SSID3'] = list_ssid3[0]
        print(json.dumps(saida['Status Base Port']['Configuração Avançada']))

    def capturaAvancada2(self):
        driver.find_element(by=By.ID, value='divMenu').click()
        sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[15]/a').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/ul/li[15]/ul/li[3]/a').click()
        driver.implicitly_wait(0.5)

        ssid = driver.find_element(by=By.ID, value='txtSsid_0').get_attribute("value")
        div = ssid.split('\n')
        sleep(6)
        ssid1 = driver.find_element(by=By.ID, value='txtSsid_1').get_attribute("value")
        div1 = ssid1.split('\n')
        sleep(6)
        ssid2 = driver.find_element(by=By.ID, value='txtSsid_2').get_attribute("value")
        div2 = ssid2.split('\n')
        sleep(3)
        ssid3 = driver.find_element(by=By.ID, value='txtSsid_3').get_attribute("value")
        div3 = ssid3.split('\n')
        sleep(3)
        saida['Status Base Port']['Configuração Avançada']['Wifi2']['SSID'] = div[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi2']['SSID1'] = div1[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi2']['SSID2'] = div2[0]
        saida['Status Base Port']['Configuração Avançada']['Wifi2']['SSID3'] = div3[0]
        print(json.dumps(saida['Status Base Port']['Configuração Avançada']))

        js = json.dumps(saida, ensure_ascii=False)
        fp = open('dados.json', 'w', encoding='utf8')
        fp.write(js)
        fp.close()


if __name__ == '__main__':
    print(str(datetime.now()) + "█▇▆▅▄▃▂▁🤖Auto teste Iniciado🤖▁▂▃▄▅▆▇█")
    selenium = selenium()
    selenium.verifyOs()
    selenium.acessoWebBasePort('http://192.168.15.190/', '78fHbmd5')
    sleep(3)
    selenium.atualizacaoFw()
    sleep(3)
    selenium.acessoWebBasePort('http://192.168.15.190/', '78fHbmd5')
    sleep(3)
    selenium.capturaWifi5Ghz()
    sleep(3)
    selenium.capturaWifi()
    sleep(3)
    selenium.capturaRoaming()
    sleep(3)
    selenium.capturaInfoDispositivos()
    sleep(3)
    selenium.capturaRedeLocal()
    sleep(3)
    selenium.capturaAvancada()
    sleep(3)
    selenium.capturaAvancada2()
    print(str(datetime.now()) + "█▇▆▅▄▃▂▁🤖Auto teste Finalizado🤖▁▂▃▄▅▆▇█")
#