exchange_rates={
  "pesos":0.00023,
  "soles":0.26538,
  "reais":0.16516
}
a=int(input("money from colombia(in pesos):"))
b=int(input("money from peru(in soles):"))
c=int(input("money from brazil(in reais):"))
colombian_usd=a* exchange_rates["pesos"]
peru_usd=b*exchange_rates["soles"]
brazil_usd=c*exchange_rates["reais"]
print("Left money from colombia",colombian_usd)
print("Left money from peru",peru_usd)
print("Left money from brazil",brazil_usd)