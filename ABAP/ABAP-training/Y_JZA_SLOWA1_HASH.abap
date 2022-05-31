*&---------------------------------------------------------------------*
*& Report
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT y_jza_slowa1_hash.



TYPES:
  BEGIN OF line,
    group TYPE i,
    pos   TYPE i,
    row   TYPE string,
  END OF line,

  BEGIN OF word_desc,
    word          TYPE string, "slowo
    count         TYPE i, "czestosc w tekscie
    in_dictionary TYPE flag_x, "czy jest w slowniku
  END OF word_desc.


*DATA: gt_occured_word TYPE STANDARD TABLE OF word_desc.
DATA gt_occured_word TYPE hashed TABLE OF word_desc    with unique key word. "klucz moze miec wiele pól
DATA gt_dict_word    TYPE hashed TABLE OF yjza_english with unique key word.

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
                                'But there is no doubt in my mind that the lion belongs with it even if he cannot reveal ' && cl_abap_char_utilities=>newline &&
                                '  himself to the eye all at once because' &
                                 ' of his huge dimension. We see him only the way a louse sitting upon him would.' )

       ).




field-Symbols: <any> type any,
               <tab> type any table,
               <fs>  type char40,
               <line> type line.

select *
  from yjza_english
  into CORRESPONDING FIELDS OF table gt_dict_word.

WRITE: / 'Tekst: ', it_text[ 1 ]-group, it_text[ 1 ]-pos, it_text[ 1 ]-row.

DATA wa_text TYPE string.
DATA lv_word_desc TYPE word_desc.
DATA lv_text_word TYPE string.

DATA wa_word LIKE LINE OF gt_occured_word.


LOOP AT it_text ASSIGNING <line>. "INTO DATA(wa_text_struc).
  WRITE: / ' '.
  WRITE: / sy-tabix, <line>-group, <line>-pos, <line>-row.
  "usun separatory
  TRANSLATE <line>-row USING '— . , ; : - = '. "a->x b->y  'axby'
  " podziel tekst na slowa
  SPLIT <line>-row AT ' ' INTO TABLE DATA(lt_words).
*  delete table lt_words where ...
  LOOP AT lt_words ASSIGNING FIELD-SYMBOL(<row>).
    check <row> is not initial.
    clear wa_word.
    wa_word-word = to_lower( <row> ).
    "sprawdz czy jest juz w tabeli
    READ TABLE gt_occured_word WITH TABLE KEY word = wa_word-word ASSIGNING FIELD-SYMBOL(<found_word>).
    IF sy-subrc EQ 0.
      "znaleziono
      ADD 1 TO <found_word>-count.
    ELSE.
      wa_word-count = 1.
      "dla kazdego slowa wypisz czy jest w slowniku. (SQL)

      read table gt_dict_word with table key word = wa_word-word TRANSPORTING no FIELDS.
*      SELECT SINGLE slowo
*      FROM yjza_palindromy
*      WHERE slowo = @wa_word-word
*        INTO @DATA(db_word).

      IF sy-subrc EQ 0.
        wa_word-in_dictionary = 'X'.
      ENDIF.

*      APPEND wa_word TO  gt_occured_word. " bl¹d gdy tabela jest typu sorted albo hashed
      insert wa_word into table gt_occured_word.
    ENDIF.

  ENDLOOP.

ENDLOOP.

"Wypisz czestosc wystepowania s³ów od najczestszych

*cl_demo_output=>display( it_text ).

data gt_occured_word2 type standard table of word_desc.

gt_occured_word2[] = gt_occured_word[].

*insert lines of gt_occured_word into table gt_occured_word2.

SORT gt_occured_word2 BY  count DESCENDING word ASCENDING.

*cl_demo_output=>display( gt_occured_word2 ).

"=================================================================================
DATA gt_dict_word    TYPE hashed TABLE OF yjza_english with unique key word.
select *
  from yjza_english
  into CORRESPONDING FIELDS OF table gt_dict_word.

data p_num type int4 value 10000. "ilosc powtorzen to parametr
do p_num time.
  read table gt_dict_word with table key word = 'zoo' TRANSPORTING no FIELDS.
enddo.

do p_num time.
  read table gt_dict_word with table key word = 'xxxxxx' TRANSPORTING no FIELDS.
enddo.