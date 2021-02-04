import csv
with open('insurance.csv') as insurance_file:
    insurance_content = csv.DictReader(insurance_file)
    count = {'with_child': 0, 'else': 0}
    age_total = {'with_child': 0, 'else': 0}
    areas_dict = {} #{area1: num_of_repeatetions}
    smoker_dict = {'smoker': [0, 0, 0], 'non': [0, 0, 0]} #{'smoker': [total_cost, num_male, num_female], 'non': [total_cost, num_male, num_female]}
    gender_cost_dict = {} #{cost1: gender1, cost2: gender2}
    gen_count = 0
    
    for row in insurance_content:
        if row['children'] == '1':
            count['with_child'] += 1
            age_total['with_child'] += int(row['age'])
        else:
            count['else'] += 1
            age_total['else'] += int(row['age'])
            
        try:
            areas_dict[row['region']] += 1
        except:
            areas_dict[row['region']] = 1
            
        if row['smoker'] == 'yes':
            smoker_dict['smoker'][0] += float(row['charges'])
            if row['sex'] == 'male':
                smoker_dict['smoker'][1] += 1
            else:
                smoker_dict['smoker'][2] += 1
        else:
            smoker_dict['non'][0] += float(row['charges'])
            if row['sex'] == 'male':
                smoker_dict['non'][1] += 1
            else:
                smoker_dict['non'][2] += 1 
        gender_cost_dict[float(row['charges'])] = row['sex']
        gen_count += 1


average_age = (age_total['with_child'] + age_total['else']) / (count['with_child'] + count['else'])
average_age_child = age_total['with_child'] / count['with_child']

most_area = 0
for key, value in areas_dict.items():
    if value > most_area:
        most_area = value
        pop_area = key

average_cost_smoker = smoker_dict['smoker'][0] / (smoker_dict['smoker'][1] + smoker_dict['smoker'][2])
average_cost_non = smoker_dict['non'][0] / (smoker_dict['non'][1] + smoker_dict['non'][2])
female_tot = smoker_dict['smoker'][2] + smoker_dict['non'][2]
male_tot = smoker_dict['smoker'][1] + smoker_dict['non'][1]

top_5per = {'male': 0, 'female': 0}
i = 0
for key in sorted(gender_cost_dict.keys()):
    if gender_cost_dict[key] == 'male':
        top_5per['male'] += 1
    else:
        top_5per['female'] += 1
    i += 1
    if i >= int(gen_count*5/100):
        break


print('The average age of sample is: {0}'.format(average_age))
print('The majority of the sample are from: ' + pop_area)
print('The average charges for smokers is {0}, while for non-smokers its {1}'.format(int(average_cost_smoker), int(average_cost_non)))
print('The average age of people with a child in sample is: {0}'.format(average_age_child))
print('For every male smoker, there is {0} female smokers'.format(smoker_dict['smoker'][2] / smoker_dict['smoker'][1]))
print('{0} of females are in the top 5% and {1} of males are in the top 5%'.format(top_5per['female'], top_5per['male']))
