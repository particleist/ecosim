# Datacard file
# Each such file must define a single routine 'data' which returns the payload
#
# This is the datacard for Great Britain 2016

def data() :
  payload = {}

  # Demographics numbers are in millions
  payload["demographics"]                         = {}
  payload["demographics"]["minors"]               = 14
  payload["demographics"]["adults"]               = 50
  payload["demographics"]["workers"]              = 32.5
  payload["demographics"]["unemployed"]           = 2.5
  payload["demographics"]["pensioners"]           = 10.5
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

  # Job type numbers, in fraction of workers
  payload["jobs"]                                 = {}
  payload["jobs"]["public_sector"]                = 0.18
  payload["jobs"]["immigrant"]                    = 0.10
  payload["jobs"]["unemployed"]                   = 0.06
  payload["jobs"]["inactive"]                     = 0.22
  
  # Immigration numbers
  
  return payload
