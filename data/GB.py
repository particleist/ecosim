# Datacard file
# Each such file must define a single routine 'data' which returns the payload
#
# This is the datacard for Great Britain 2016
#
# Stats taken from https://www.nomisweb.co.uk/reports/lmp/gor/2092957698/report.aspx

def data() :
  payload = {}

  # Demographics numbers are in millions
  payload["demographics"]                         = {}
  payload["demographics"]["minors"]               = 12
  payload["demographics"]["adults"]               = 52
  payload["demographics"]["workers"]              = 31
  payload["demographics"]["unemployed"]           = 2
  payload["demographics"]["inactive"]             = 9
  payload["demographics"]["pensioners"]           = 10
  # Note, disabled here does NOT mean unable to work
  # But we can assume that this fraction of the population
  # will need some additional support from the state
  payload["demographics"]["disabled"]             = 10

  # Budget numbers are in billions
  payload["budget"]                               = {}
  payload["budget"]["social_protection"]          = 240
  payload["budget"]["personal_social_services"]   = 0
  payload["budget"]["housing_environment"]        = 34
  payload["budget"]["education"]                  = 102
  payload["budget"]["health"]                     = 145
  payload["budget"]["defence"]                    = 46
  payload["budget"]["police"]                     = 34
  payload["budget"]["transport"]                  = 29
  payload["budget"]["industry_agriculture"]       = 24
  payload["budget"]["other"]                      = 49

  # Revenue numbers are in billions
  payload["revenue"]                              = {}
  payload["revenue"]["income_tax"]                = 182
  payload["revenue"]["vat"]                       = 138
  payload["revenue"]["national_insurance"]        = 126
  payload["revenue"]["excise"]                    = 48
  payload["revenue"]["corporate_tax"]             = 43
  payload["revenue"]["council_tax"]               = 30
  payload["revenue"]["business_rates"]            = 28
  payload["revenue"]["other"]                     = 120

  # Housing numbers are in millions of households
  payload["housing"]                              = {}
  payload["housing"]["homeowners"]                = 7
  payload["housing"]["mortgaged"]                 = 8
  payload["housing"]["renting_social"]            = 3.7
  payload["housing"]["renting_private"]           = 3.3
  payload["housing"]["empty"]                     = 0.7
  payload["housing"]["singles"]                   = 5.9
  payload["housing"]["couples"]                   = 7.8
  payload["housing"]["parents"]                   = 4.5

  # Job type numbers, in millions
  payload["jobs"]                                 = {}
  payload["jobs"]["public_sector"]                = 6
  payload["jobs"]["immigrant"]                    = 3
  # The following categories are in essentially ordered
  # in descending salary brackets
  payload["jobs"]["managers"]                     = 3.2
  payload["jobs"]["professional"]                 = 6.2
  payload["jobs"]["technical"]                    = 4.4
  payload["jobs"]["admin"]                        = 3.3
  payload["jobs"]["skilled_trade"]                = 3.3
  payload["jobs"]["caring_leisure"]               = 2.9
  payload["jobs"]["sales_customer"]               = 2.4
  payload["jobs"]["machine_operators"]            = 2
  payload["jobs"]["unskilled"]                    = 3.4
  
  # Immigration 
  # For now, as immigrants begin as only 10% of workforce, will
  # simply assume they are distributed in the same proportion among
  # the job categories as the full population
  # Similarly will assume the public sector jobs are divided among
  # categories in the same proportion as the entire market
  
  return payload
