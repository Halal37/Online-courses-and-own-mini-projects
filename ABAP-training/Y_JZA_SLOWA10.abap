*&---------------------------------------------------------------------*
*& Report
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT Y_JZA_SLOWA10.



TYPES:
  BEGIN OF line,
    group type i,
    pos   TYPE i,
    row   TYPE string,
  END OF line,

  BEGIN OF word_desc,
    word      type string,
    count     TYPE i,
    in_dictionary  TYPE flag_X,
  END OF word_desc.
  .

data: gt_occured_word type standard table of word_desc.


DATA: it_text  TYPE STANDARD TABLE OF line.


it_text = VALUE #(
      ( group = 1 pos = 1 row = 'A happy man is too satisfied with the present to dwell too much on the future.' )
      ( group = 2 pos = 1 row = 'It followed from the special theory of relativity that mass and energy are both but ' )
      ( group = 2 pos = 2 row = 'different manifestations of the same thing — a somewhat unfamiliar conception for the average mind. '  &&
               'Furthermore, the equation E = mc2, in which energy is put equal to mass, multiplied by the square of the velocity of light, '  &&
               'showed that very small amounts of mass may be converted into a very large amount of energy and vice versa. The mass and energy '  &&
               'were in fact equivalent, according to the formula mentioned before. This was demonstrated by Cockcroft and Walton in 1932, experimentally.' )
      ( group = 3 pos = 1 row = 'The mass of a body is a measure of its energy content.' )

      ( group = 4 pos = 1 row = 'Nature shows us only the tail of the lion. ' && cl_abap_char_utilities=>cr_lf &&
                                'But there is no doubt in my mind that the lion belongs with it even if he cannot reveal ' && cl_abap_char_utilities=>NEWLINE &&
                                '  himself to the eye all at once because' &
                                 ' of his huge dimension. We see him only the way a louse sitting upon him would.' )

       ).


data it_dict_word type standard table of YJZA_ENGLISH.

write: / 'Tekst: ', it_text[ 1 ]-group, it_text[ 1 ]-pos, it_text[ 1 ]-row.

data wa_text type string.
data lv_word_desc type word_desc.
data lv_text_word type string.


loop at it_text into data(wa_text_struc).
  write: SY-TABIX, wa_text_struc-GROUP, wa_text_struc-POS, wa_text_struc-row.
  "usun separatory
   TRANSLATE wa_text_struc-row USING '. , ; : - '.
 " podziel tekst na slowa
    split wa_text_struc-row at ' ' into table data(lt_words).
  "dla kazdego slowa wypisz czy jest w slowniku. (SQL)
    loop at lt_words into lv_text_word.


      select single word
        from YJZA_ENGLISH
        where word = @lv_text_word
        into @data(dict_word).

      if sy-subrc EQ 0.
        lv_word_desc-IN_DICTIONARY = 'X'.
      else.
        lv_word_desc-IN_DICTIONARY = ''.
      endif.
      lv_word_desc-COUNT = 1.
      lv_word_desc-WORD = lv_text_word.

  "dla kazdego slowa zlicz ile razy wystapilo w przetwarzanym tekscie
      Read table gt_occured_word with key word = lv_word_desc-WORD ASSIGNING FIELD-SYMBOL(<slowo>).
      if sy-subrc EQ 0.
         add 1 to <slowo>-COUNT.
      else.
        insert lv_word_desc into table gt_occured_word.
      endif.

     endloop.




endloop.
"Wypisz czestosc wystepowania s³ów od najczestszych

*cl_demo_output=>display( it_text ).
sort GT_OCCURED_WORD by count DESCENDING.

*cl_demo_output=>display( GT_OCCURED_WORD ).

* select word
*  from YJZA_ENGLISH
*  into table @data(it_dict_word).