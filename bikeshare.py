import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

CITY_NAME = { 'ch': 'Chicago',
              'ny': 'New York City',
              'wa': 'Washington' }

MONTHS_DATA = { 'ja': 1,
                'fe': 2,
                'ma': 3,
                'ap': 4,
                'my': 5,
                'ju': 6 }

MONTHS_NAME = { 'ja': 'January',
                'fe': 'February',
                'ma': 'March',
                'ap': 'April',
                'my': 'May',
                'ju': 'June' }

MONTHS_NUMBER = { 1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June' }

DAYS_DATA = { 'su': 'Sunday',
              'mo': 'Monday',
              'tu': 'Tuesday',
              'we': 'Wednesday',
              'th': 'Thursday',
              'fr': 'Friday',
              'sa': 'Saturday' }

def get_started():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) icity - name of the city to analyze
        (df) df - Pandas Dataframe containing city data filtered by month and day
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).

    icity = ''
    while icity != 'ch' and icity != 'ny' and icity != 'wa':
        icity = input("Select which city you'd like to analyze. Type 'Ch' for Chicago, 'Ny' for New York City and 'Wa' for Washington. (Please only type the letters, ex: Ch): ").lower()
        if icity == 'ch' or icity == 'ny' or icity == 'wa':
            break
        else:
            print("\nYour input isn't valid, please try again")
            continue

    df = pd.read_csv(CITY_DATA[icity],sep=',')
    print("Thank you for your input, the city selected is: {}".format(CITY_NAME[icity]))

    # get user input for month (all, january, february, ... , june)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month

    imonth = ''
    while imonth != 'all' and imonth != 'ja' and imonth != 'fe' and imonth != 'ma' and imonth != 'ap' and imonth != 'my' and imonth != 'ju':
        imonth = input("\nSelect which month you'd like to see the data for. Type 'Ja' for January, 'Fe' for February, 'Ma' for March, 'Ap' for April, 'My' for May and 'Ju' for June. If you'd like to see the data for all the months type 'All' . (Please only type the letters, ex: Ju): ").lower()
        if imonth == 'ja' or imonth == 'fe' or imonth == 'ma' or imonth == 'ap' or imonth == 'my' or imonth == 'ju':
            df = df[(df['Month'] == MONTHS_DATA[imonth])]
            print("\nThank you for your imput, the month selected was: {}".format(MONTHS_NAME[imonth]))
            break
        elif imonth == 'all':
            df = df
            print("\nThank you for your input, all months were selected!")
        else:
            print("\nYour input isn't valid, please try again")
            continue    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    df['day_of_week'] = df['Start Time'].dt.day_name()

    iday = ''
    while iday != 'all' and iday != 'su' and iday != 'mo' and iday != 'tu' and iday != 'we' and iday != 'th' and iday != 'fr' and iday != 'sa':
        iday = input("\nSelect which day you'd like to see data for. Type 'Su' for Sunday, 'Mo' for Monday, 'Tu' for Tuesday, 'We' for Wednesday, 'Th' for Thursday, 'Fr' for Friday and 'Sa' for Saturday. If you'd like to see the data for all the days type 'All' (Please only type the letters, ex: All): ").lower()
        if iday == 'su' or iday == 'mo' or iday == 'tu' or iday == 'we' or iday == 'th' or iday == 'fr' or iday == 'sa':
            df = df[(df['day_of_week'] == DAYS_DATA[iday])]
            print("\nThank you for your imput, the week day selected was: {}".format(DAYS_DATA[iday]))
            break
        elif iday == 'all':
            df = df
            print("\nThank you for your imput, all week days were selected")
        else:
            print("\nYour input isn't valid, please try again")
            continue

    print('-'*40)
    print('\nThank you for your input user. We are ready to start the analysis')
    return df, icity



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = pd.Series(df['Month'])

    # display the most common month
    modemonth = months.mode()[0]
    print('The most common month of travel is: {}'.format(MONTHS_NUMBER[modemonth]))

    # display the most common day of week
    modeweekday = df['day_of_week'].mode()[1]
    print('The most common weekday is: {}'.format(modeweekday))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    hourmode = df['Start Time'].dt.hour.mode()[1]
    print('The most common hour is: {}'.format(hourmode))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    modestartstation = df['Start Station'].mode()[0]
    print('The most common Start Sation is: {}'.format(modestartstation))

    # display most commonly used end station
    modeendstation = df['End Station'].mode()[0]
    print('The most common End Sation is: {}'.format(modeendstation))

    # display most frequent combination of start station and end station trip
    df['Trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    modetrip = df['Trip'].mode()[0]
    print('The most common Trip is: {}'.format(modetrip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totaltriptime = df['Trip Duration'].sum().sum()
    hour = totaltriptime // 3600
    minutes = (totaltriptime - hour * 3600) // 60
    seconds = (totaltriptime - hour * 3600 - minutes * 60)
    converted_totaltriptime = "{} hours {} minutes and {} seconds".format(hour, minutes, seconds)
    print('The total trip time is: {}'.format(converted_totaltriptime))

    # display mean travel time
    meantriptime = df['Trip Duration'].mean().mean()
    hour2 = totaltriptime // 3600
    minutes2 = (totaltriptime - hour * 3600) // 60
    seconds2 = (totaltriptime - hour * 3600 - minutes * 60)
    converted_meantriptime = "{} hours {} minutes and {} seconds".format(hour2, minutes2, seconds2)
    print('The average trip duration is: {}'.format(converted_meantriptime))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    countusertypes = df['User Type'].value_counts()
    print(countusertypes)

    # Display counts of gender
    countgendertypes = df['Gender'].value_counts()
    print(countgendertypes)

    # Display earliest, most recent, and most common year of birth
    oldestclients = int(df['Birth Year'].min())
    youngestclients = int(df['Birth Year'].max())
    modeclients = int(df['Birth Year'].mode())
    print('The earliest year of birth we have among our clients is: {}'.format(oldestclients))
    print('The latest year of birth we have among our clients is: {}'.format(youngestclients))
    print('The most common year of birth we have among our clients is: {}'.format(modeclients))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    """
    Displays the rows of the dataframe in clusters of 5 rows until the user asks to stop.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        df - Rows of the panda's dataframe in clusters of 5 until the user asks to stop
    """
    view_data = ''
    start_loc = 0
    dfrows = df.shape[0]
    pd.set_option('display.max_columns',dfrows)
    while view_data != 'no':
        view_data = input('\nWould you like to view 5 rows of individual trip data? Please type yes to confirm or no to refuse: ').lower()
        if view_data == 'yes':
            while view_data == 'yes':
                print(df.iloc[start_loc:(start_loc + 5)])
                start_loc += 5
                view_data = input('\nDo you wish to see 5 more rows?  Please type yes to confirm or no to refuse: ')
                if view_data == 'no':
                    break
                elif view_data != 'yes' and view_data != 'no':
                    print("\nYour input isn't valid, please try again")
        elif view_data != 'yes' and view_data != 'no':
            print("\nYour input isn't valid, please try again")
            continue            

def main():
    while True:
        df, icity = get_started()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if icity != 'wa':
            user_stats(df)
        display(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'yes':
            continue
        else:        
            while restart != 'yes' and restart != 'no':
                print("\nYour input isn't valid, please try again")
                restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
                if restart == 'yes' or restart != 'no':
                    break
            if restart != 'yes':
                print("\nThank you for your input!\nEnding program!")
                break
            else:
                print("\nThank you for your input!\nRestarting program!")
                continue

if __name__ == "__main__":
	main()
