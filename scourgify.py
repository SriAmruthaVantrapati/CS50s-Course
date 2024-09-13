import csv
import sys
def main():
    if len(sys.argv) == 3 :
       if sys.argv[1].find('.csv') != -1 or sys.argv[2].find('.csv') != -1 :
        try:
           write_file((swap_name()))

        except FileNotFoundError :
         print(f'Could not read {sys.argv[1]}')
         sys.exit(1)
       else :
         print('Not a CSV file')
         sys.exit(1)

    elif len(sys.argv) < 3 :
     print('Too few command-line arguments')
     sys.exit(1)
    elif len(sys.argv) > 3 :
     print('Too many command-line arguments')
     sys.exit(1)

def swap_name():
           name_list = []
           with open(sys.argv[1],'r') as file:
            reader = csv.DictReader(file)
            for row in reader :
               split_name = row["name"].split(",")
               name_list.append({"first":split_name[1].lstrip(),"last":split_name[0],"house":row["house"]})
            return(name_list)


def write_file(list):
   with open(sys.argv[2],"w") as file :
      writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
      writer.writerow({"first":"first","last":"last","house":"house"})
      for row in list :
         writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})


if __name__=="__main__":
  main()
