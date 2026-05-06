print('Study Tracker\n')

study_graph = []

def add_study():
    subject = input('Which subject do you studied:')
    time = input('do much time do you studied:')
    day = input('Which day:')
    study_graph.append({'Subject': subject,'Time' : time,'Day': day})
    save_graph(subject,time,day)
    print('Added!')


def view_graph():
    for s in study_graph:
        print(s['Subject'],':',s['Time'],':',s['Day'])


def save_graph(subject,time,day):
    f = open('study.txt','a')
    f.write(f'{subject},{time},{day}\n')
    f.close()


def load_schedule():
    f = open('study.txt','r')
    text = f.read()
    print(text)
    f.close()

def remove():
    remove = input('What do you want to delete:')
    for s in study_graph:
        if s['Subject'] == remove:
            study_graph.remove(s)
            print('Deleted!')


while True:
    print('1. Add sub/time/day')
    print('2. Add view schedule')
    print('3. load schedule')
    print('4. delete schedule')

    user = input('Choose(1/2/3/4):')
    if user == '1':
        add_study()

    elif user == '2':
        view_graph()


    elif user == '3':
        load_schedule()


    elif user == '4':
        remove()


    cont = input('Do you want to continue(yes/no):').lower()
    if cont == 'no':
        print('Thankyou!')
        break
























































