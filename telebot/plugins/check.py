from keystoneauth1.identity import v3
from keystoneauth1 import session
from neutronclient.v2_0 import client
from prettytable import PrettyTable
import novaclient.client as novaclient

def authenticate():
    IP = '192.168.100.48'
    USERNAME = 'admin'
    PASSWORD = 'minhkma'
    PROJECT_NAME = 'admin'
    AUTH_URL = 'http://{}/identity/v3'.format(IP)
    auth = v3.Password(auth_url=AUTH_URL,
                       user_domain_name='default',
                       username=USERNAME,password=PASSWORD,
                       project_domain_name='default',
                       project_name=PROJECT_NAME)
    sess = session.Session(auth=auth)
    return sess

def handle(bot, update, args):
    msg_neutron = ''
    sess = authenticate()
    neutron = client.Client(session=sess)
    table_networks = PrettyTable(['ID', 'Name', 'subnets'])
    networks = neutron.list_networks()
    for i in range(len(networks["networks"])):
        Name = networks["networks"][i]["name"]
        ID = networks["networks"][i]["id"]
        subnets = networks["networks"][0]["subnets"][0]
        table_networks.add_row([ID, Name, subnets])
    msg_neutron = msg_neutron + str(table_networks) + '\n'
    table_agents = PrettyTable(['ID', 'Agent Type', 'Host', 'Availability Zone', 'Alive', 'State', 'Binary'])
    agents = neutron.list_agents()
    for count_agents in range(len(agents['agents'])):
        ID = agents['agents'][count_agents]['id']
        Agent_type = agents['agents'][count_agents]['agent_type']
        Host = agents['agents'][count_agents]['host']
        Availability_Zone = agents['agents'][count_agents]['availability_zone']
        Alive = agents['agents'][count_agents]['alive']
        Admin_state_up = agents['agents'][count_agents]['admin_state_up']
        if Admin_state_up == True:
           State = ':)'
        else:
          State = ':('
        Binary = agents['agents'][count_agents]['binary']
        table_agents.add_row([ID, Agent_type, Host, Availability_Zone, Alive, State, Binary])
    msg_neutron = msg_neutron + str(table_agents) + '\n'
    msg_nova = ''
    sess = authenticate()
    nova = novaclient.Client("2.1", session=sess)
    tables_servers = PrettyTable(['Name_instance', 'status'])
    server_list = nova.servers.list()
    for count_server,i in enumerate(server_list):
        Name_instance = server_list[count_server].name
        status = server_list[count_server].status
        tables_servers.add_row([Name_instance, status])
    msg_nova = msg_nova + str(tables_servers) + '\n'
    tables_services = PrettyTable(['binary', 'host', 'status', 'state', 'zone'])
    services = nova.services.list()
    for count_services,j in enumerate(services):
        data_dict = services[count_services]._info
        binary = data_dict['binary']
        host = data_dict['host']
        status = data_dict['status']
        state = data_dict['state']
        zone = data_dict['zone']
        tables_services.add_row([binary, host, status, state, zone])
    msg_nova = msg_nova + str(tables_services) + '\n'
    tables_flavors = PrettyTable(['ID', 'Name', 'Memory_MB', 'Disk', 'Ephemeral',
                                  'Swap', 'VCPUsRXTX_Factor', 'Is_Public'])
    flavors = nova.flavors.list()
    for count_flavors,k in enumerate(flavors):
        data_favors = flavors[count_flavors]._info
        ID = data_favors['id']
        Name = data_favors['name']
        Memory_MB = data_favors['ram']
        Disk = data_favors['disk']
        Ephemeral = data_favors['OS-FLV-EXT-DATA:ephemeral']
        Swap = data_favors['swap']
        VCPUsRXTX_Factor = data_favors['vcpus']
        Is_Public = data_favors['os-flavor-access:is_public']
        tables_flavors.add_row([ ID, Name, Memory_MB, Disk, Ephemeral, Swap, VCPUsRXTX_Factor, Is_Public])
    msg_nova = msg_nova + str(tables_flavors) + '\n'
    try:
        action = args.pop(0)
        if action == 'nova':
            update.message.reply_text(msg_nova)
            return
        if action == 'neutron':
            update.message.reply_text(msg_neutron)
            return
        else:
            raise ValueError
    except(IndexError, ValueError):
        update.message.reply_text('Usage: /check status')


