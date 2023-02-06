#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-12-07 22:25:22
# @Author  : Adam Wen (adamwen829@gmail.com)
import json
from copy import deepcopy
from enum import Enum

import yaml


class NameDescriptor:
    @classmethod
    def convert_name(cls, name):
        if name == 'Auto_UrlTest':
            return "Auto - UrlTest"
        return name.replace('_', ' ')
        

    def __init__(self, name, value):
        self.name = self.convert_name(name)
        self.value = value
    
    def __get__(self, instance, owner):
        # Return the name and value as a tuple
        return self

class RuleSetMeta(type):
    def __new__(cls, clsname, bases, attrs):
        l = []
        for name, value in attrs.items():
            if not name.startswith('__'):
                # Set the attribute as a NameDescriptor instance
                attrs[name] = NameDescriptor(name, value)
                l.append(attrs[name])
        attrs['__members__'] = l
        return type.__new__(cls, clsname, bases, attrs)
    

DEFAULT_RULE_INTERVAL = 86400


with open('./proxy_providers.json', 'r') as f:
    PROXY_PROVIDERS = json.load(f)


class RuleSet(metaclass=RuleSetMeta):
    Auto_UrlTest = {
        "proxies": [],
        'type': 'url-test',
        'url': 'http://cp.cloudflare.com/generate_204',
        'interval': '3600'
    }
    Proxy = {"proxies": ["DIRECT"]}
    Domestic = {"proxies": ["DIRECT", "Proxy"]}
    Others = {"proxies": ["Proxy", "DIRECT"]}
    Duolingo = {"proxies": ["DIRECT", "Proxy"]}
    Apple_News = {"proxies": ["DIRECT", "Proxy"]}
    Apple_TV = {"proxies": ["DIRECT", "Proxy"]}
    Apple_Music = {"proxies": ["DIRECT", "Proxy"]}
    DIRECT = {"proxies": ["DIRECT", "Proxy"]}
    NeteaseMusic = {"proxies": ["DIRECT", "Proxy"]}
    AdBlock = {"proxies": ["REJECT", "DIRECT", "Proxy"]}
    Apple = {"proxies": ["DIRECT", "Proxy"]}
    Google_FCM = {"proxies": ["Proxy", "DIRECT"]}
    Scholar = {"proxies": ["DIRECT", "Proxy"]}
    Asian_TV = {"proxies": ["DIRECT", "Proxy"]}
    Global_TV = {"proxies": ["Proxy", "DIRECT"]}
    Netflix = {"proxies": ["Proxy", "DIRECT"]}
    Disney = {"proxies": ["Proxy", "DIRECT"]}
    Spotify = {"proxies": ["Proxy", "DIRECT"]}
    YouTube = {"proxies": ["Proxy", "DIRECT"]}
    Telegram = {"proxies": ["Proxy", "DIRECT"]}
    Crypto = {"proxies": ["Proxy", "DIRECT"]}
    Discord = {"proxies": ["Proxy", "DIRECT"]}
    Steam = {"proxies": ["Proxy", "DIRECT"]}
    Speedtest = {"proxies": ["Proxy", "DIRECT"]}
    PayPal = {"proxies": ["DIRECT", "Proxy"]}
    Microsoft = {"proxies": ["DIRECT", "Proxy"]}


RULES_IN = {
    'Reject': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Reject.yaml',
        'rule-set': RuleSet.AdBlock
    },
    'Duolingo': {
        'url': 'https://cdn.jsdelivr.net/gh/adamwen829/myrc@3337939952e961ed8ed1488a3f103323a68e10fc/clash/duolingo.yaml',
        'rule-set': RuleSet.Duolingo
    },
    'Special': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Special.yaml',
        'rule-set': RuleSet.DIRECT
    },
    'Netflix': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Netflix.yaml',
        'rule-set': RuleSet.Netflix
    },
    'Spotify': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Spotify.yaml',
        'rule-set': RuleSet.Spotify
    },
    'YouTube': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/YouTube.yaml',
        'rule-set': RuleSet.YouTube
    },
    'Bilibili': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Bilibili.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'IQ': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/IQ.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'IQIYI': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/IQIYI.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'Letv': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Letv.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'Netease Music': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Netease%20Music.yaml',
        'rule-set': RuleSet.NeteaseMusic
    },
    'Tencent Video': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Tencent%20Video.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'Youku': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Youku.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'WeTV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/WeTV.yaml',
        'rule-set': RuleSet.Asian_TV
    },
    'ABC': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/ABC.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Abema TV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Abema%20TV.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Amazon': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Amazon.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Apple Music': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Apple%20Music.yaml',
        'rule-set': RuleSet.Apple_Music
    },
    'Apple News': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Apple%20News.yaml',
        'rule-set': RuleSet.Apple_News
    },
    'Apple TV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Apple%20TV.yaml',
        'rule-set': RuleSet.Apple_TV
    },
    'Bahamut': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Bahamut.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'BBC iPlayer': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/BBC%20iPlayer.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'DAZN': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/DAZN.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Discovery Plus': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Discovery%20Plus.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Disney Plus': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Disney%20Plus.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'encoreTVB': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/encoreTVB.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'F1 TV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/F1%20TV.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Fox Now': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Fox%20Now.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Fox+': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Fox%2B.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'HBO Go': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/HBO%20Go.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'HBO Max': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/HBO%20Max.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Hulu Japan': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Hulu%20Japan.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Hulu': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Hulu.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Japonx': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Japonx.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'JOOX': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/JOOX.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'KKBOX': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/KKBOX.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'KKTV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/KKTV.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Line TV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Line%20TV.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'myTV SUPER': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/myTV%20SUPER.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Niconico': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Niconico.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Pandora': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Pandora.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'PBS': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/PBS.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Pornhub': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Pornhub.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Soundcloud': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/Soundcloud.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'ViuTV': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Media/ViuTV.yaml',
        'rule-set': RuleSet.Global_TV
    },
    'Telegram': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Telegram.yaml',
        'rule-set': RuleSet.Telegram
    },
    'Crypto': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Crypto.yaml',
        'rule-set': RuleSet.Crypto
    },
    'Discord': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Discord.yaml',
        'rule-set': RuleSet.Discord
    },
    'Steam': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Steam.yaml',
        'rule-set': RuleSet.Steam
    },
    'Speedtest': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Speedtest.yaml',
        'rule-set': RuleSet.Discord
    },
    'PayPal': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/PayPal.yaml',
        'rule-set': RuleSet.PayPal
    },
    'Microsoft': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Microsoft.yaml',
        'rule-set': RuleSet.Microsoft
    },
    'PROXY': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Proxy.yaml',
        'rule-set': RuleSet.Proxy
    },
    'Domestic': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Domestic.yaml',
        'rule-set': RuleSet.Domestic
    },
    'Apple': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Apple.yaml',
        'rule-set': RuleSet.Apple
    },
    'Google FCM': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Google%20FCM.yaml',
        'rule-set': RuleSet.Google_FCM
    },
    'Scholar': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Scholar.yaml',
        'rule-set': RuleSet.Scholar
    },
    'Domestic IPs': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/Domestic%20IPs.yaml',
        'behavior': 'ipcidr',
        'rule-set': RuleSet.Domestic
    },
    'LAN': {
        'url':
        'https://fastly.jsdelivr.net/gh/dler-io/Rules@main/Clash/Provider/LAN.yaml',
        'rule-set': RuleSet.DIRECT
    }
}


def filename(name) -> str:
    return name.replace('_', ' ')



def generate_proxy_providers():
    configs = {}
    for name, url in PROXY_PROVIDERS.items():
        configs[name] = {
                "type": "http",
                "url": url,
                "interval": 3600,
                "path": f"./proxy_providers/{name}.yaml",
                "health-check": {
                    "enable": True,
                    "interval": 600,
                    "url": "http://www.gstatic.com/generate_204"
                }
        }
    return configs


def generate_proxy_groups():
    proxy_groups = []
    for ruleset in RuleSet.__members__:
        if ruleset == RuleSet.DIRECT:
            continue

        proxy_group = deepcopy(ruleset.value)

        if 'type' not in proxy_group:
            proxy_group['type'] = 'select'

        proxy_group['use'] = []
        for name, _ in PROXY_PROVIDERS.items():
            proxy_group['use'].append(name)
        proxy_group['name'] = ruleset.name
        if ruleset != RuleSet.Auto_UrlTest:
            proxy_group['proxies'].append(RuleSet.Auto_UrlTest.name)
        proxy_groups.append(proxy_group)

    return proxy_groups


def generate_rule_rule_providers(rules_in):
    rules = []
    for name, config in rules_in.items():
        rules.append(f"RULE-SET,{name},{config['rule-set'].name}")
    rules.extend(['GEOIP,CN,Domestic', 'MATCH,Others'])
    return rules


def generate_rule_providers(rules_in):
    rule_providers = {}
    for name, config in rules_in.items():
        rule_config = {
            "type": config.get('type', 'http'),
            "behavior": config.get('behavior', 'classical'),
            "path": f'./ruleset/{filename(name)}.yaml',
            "url": config['url'],
            "interval": config.get("interval", DEFAULT_RULE_INTERVAL)
        }
        rule_providers[name] = rule_config
    return rule_providers


def generate():
    with open('./head.yaml', 'r') as f:
        head = f.read()
    dynamic_config = {
        'proxy-providers': generate_proxy_providers(),
        'proxy-groups': generate_proxy_groups(),
        'rules': generate_rule_rule_providers(RULES_IN),
        'rule-providers': generate_rule_providers(RULES_IN),
    }
    dynamic = yaml.dump(dynamic_config, Dumper=yaml.Dumper)
    config = head+dynamic
    with open('./config.yaml', 'w') as f:
        f.write(config)


if __name__ == '__main__':
    generate()