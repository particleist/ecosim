# A configuration file for simulating basic income
# Each such configuration file defines one method, config, which returns the payload
#
# This fils 2110 corresponds to a basic income providing the full living wage, with kids paid less into a trust fund

def config() :
  payload = {}

  # Income is in millions/annum
  payload["income"]               = {}
  payload["income"]["adult"]      = 0.015
  payload["income"]["minor"]      = 0.005
  payload["income"]["minortrust"] = True

  return payload 
