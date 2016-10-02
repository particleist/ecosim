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
  # Assume that basic income will be introduced gradually over time
  # The following parameters control over how many years it is introduced
  # Clearly introducing it instantly is simply an (unrealistic) special case
  #
  # The variable gives the number of years to phase in the full income
  # the phasing is done in a uniform manner
  payload["income"]["phasing"]    = 5
  # If set to true, income of minors is given to them 
  # on their 18th birthday in the form of a trust fund
  payload["income"]["minortrust"] = True
  
  # Assumptions about automation
  payload["automation"]           = {}
  # If true, humans will be replaced by robots 
  # in certain jobs as a function of time
  payload["automation"]["use"]    = True
  # Job types to apply automation to, and 
  # probability that a job of a given type is replaced
  # in any given year
  payload["automation"]["jobs"]   = {"unskilled"          : 0.050,
                                     "machine_operators"  : 0.100,
                                     "admin"              : 0.050,
                                     "technical"          : 0.025,
                                     "skilled_trade"      : 0.010}
  # We need a critical mass beyond which automation will 
  # immediately replace all remaining jobs being done by humans in a sector
  payload["automation"]["cutoff"] = 0.75
  # We need to estimate what fraction of jobs lost to automation
  # will be recrated as technical jobs supporting automation
  payload["automation"]["feedback"] = 0.05
  
  # Assumptions about taxation
  # Assume that the govt can choose to tax
  # income more, profits more, or vat more
  # All taxes are "extra" relative to the baseline
  payload["tax"]                  = {}
  payload["tax"]["income"]        = 0.0
  payload["tax"]["profit"]        = 0.1
  payload["tax"]["vat"]           = 0.0
  
  return payload 
