Can generate a random verse, change the style of the verse and if asked (contact me) can sorte every reference of your verses. if you put your verses list in the file : versets.txt with this format : 

\someting\ #it needs 2 first lines only at the beginning
\n
\verses #then first part the citation
\references \version (THE VERSION IS NEEDED) #the reference
\n #blank line
\verses #repeat it 
\references \version
\n
\verses  
\references \version
\n
...

in the terminal : 
#don't forget to change versets.txt with your verses, it can only support french version (S21, BDS, LSG ; it's not hard to change that, contact me if necessary!!)
./formatting_verses/formatted_verse_method.sh (.zsh if using mac)
./random_verse.sh (.zsh if using mac)

Need to change the name of files
