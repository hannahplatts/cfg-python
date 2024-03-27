print('You are applying for a job that requires a drivers license. Please fill out this form:')

drive = input('Can you drive?')
can_drive = drive == 'yes'

car = input('Do you have a car?')
has_car = car == 'yes'

suitable_for_job = can_drive and has_car
print('You are suitable for the job: {}'.format(suitable_for_job))

if(suitable_for_job)