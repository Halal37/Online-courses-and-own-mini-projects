FUNCTION Y_JZA_TESTHASH10.
*"--------------------------------------------------------------------
*"*"Local Interface:
*"  IMPORTING
*"     REFERENCE(IN_NUM_REPET) TYPE  I DEFAULT 10000
*"     REFERENCE(IN_MODE) TYPE  STRING DEFAULT 'HASH'
*"--------------------------------------------------------------------

DATA lt_dict_word_std  TYPE standard TABLE OF yjza_english with non-unique key word.
DATA lt_dict_word_sort TYPE sorted TABLE OF yjza_english with unique key word.
DATA lt_dict_word_hash TYPE hashed TABLE OF yjza_english with unique key word.


select *
  from yjza_english
  into CORRESPONDING FIELDS OF table lt_dict_word_std.

case in_mode.
  when 'STANDARD' or 'STD'.

do in_num_repet times.
   read table  lt_dict_word_std with table key word = 'zimbabwe'  TRANSPORTING NO FIELDS.
enddo.

do in_num_repet times.
   read table  lt_dict_word_std with table key word = 'xxxXX'  TRANSPORTING NO FIELDS.
enddo.

when 'SORT' or 'SORTED'.

do in_num_repet times.
   read table  lt_dict_word_sort with table key word = 'zimbabwe'  TRANSPORTING NO FIELDS.
enddo.

do in_num_repet times.
   read table  lt_dict_word_sort with table key word = 'xxxXX'  TRANSPORTING NO FIELDS.
enddo.


when 'HASH' or 'HASHED'.
do in_num_repet times.
   read table  lt_dict_word_hash with table key word = 'zimbabwe'  TRANSPORTING NO FIELDS.
enddo.

do in_num_repet times.
   read table  lt_dict_word_hash with table key word = 'xxxXX'  TRANSPORTING NO FIELDS.
enddo.


WHEN OTHERS.
  message 'Blad! podaj STD, HASH or SORT' type 'E'.
endcase.


ENDFUNCTION.