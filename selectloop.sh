select makanan in babigoreng cotomakassar rotisauskurma misetan gaada
do
  case $makanan in
   babigoreng|cotomakassar)
      echo "pilihan yang tepat"
      ;;
   rotisauskurma|misetan)
      echo "kamu hebat"
      ;;
     gaada)
       break
      ;;
      *) echo "error"
      ;;
   esac
done
