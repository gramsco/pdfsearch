# pdfsearch
Merge pdfs into a single one :o

How
--
    python3 main.py [folder] [query]


Example:

    $ python3 main.py pdfs trad

    > Looking for "trad"

    || article_translation.pdf || 

         -> match on page 0
         -> match on page 1
         -> match on page 2
         -> match on page 3
         -> match on page 4
         -> match on page 5
         -> match on page 6
         -> match on page 7
         -> match on page 8

    || article_translation2.pdf || 

         -> match on page 0
         -> match on page 1
         -> match on page 2
         -> match on page 3
         -> match on page 4
         -> match on page 5
         -> match on page 6
         -> match on page 7
         -> match on page 8

    Do you want to create a file? y

        ––––––––––––––––––––––––––––––––
        trad.pdf created!
        ––––––––––––––––––––––––––––––––

    ~ bye 
