yearly_revenue = {2017 : 100000,
                  2018 : 120000,
                  2019 : 125000,
                  2020 : 110000,
                  2021 : 130000}
total_income = 0

for year_id in yearly_revenue.keys():
    total_income += yearly_revenue[year_id]
    print(year_id, yearly_revenue[year_id])

print(total_income)
print(total_income/len(yearly_revenue))
