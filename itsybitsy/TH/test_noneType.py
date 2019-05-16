my_dict = {
  "realm": "prod",
  "sitename": "wizardsmtg",
  "username": "santosh.ratnala",
  "reasonForPerfeval": {
    "downsize_risk_assessment": "Downsize Risk Assessment"
  }
}

print(my_dict)
downsize_reason = "downsize_risk_assessment" in my_dict.get('reasonForPerfeval', {})
print(downsize_reason)
downsize = my_dict.get('reasonForPerfeval', {})
print(downsize)
print(type(downsize))
