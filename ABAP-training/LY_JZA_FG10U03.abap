FUNCTION Y_JZA_PALINDROM10.
*"----------------------------------------------------------------------
*"*"Local Interface:
*"  IMPORTING
*"     REFERENCE(IN_WORD) TYPE  STRING
*"  EXPORTING
*"     REFERENCE(OUT_IS_PALINDROM) TYPE  FLAG_X
*"----------------------------------------------------------------------

data lv_slowo_odr type string.

CALL FUNCTION 'Y_JZA_REVERSE10'
EXPORTING
  IN_WORD = in_word
  IMPORTING
  OUT_WORD = lv_slowo_odr
  .

if lv_slowo_odr EQ in_word.
  OUT_IS_PALINDROM = 'X'.
  else.
    OUT_IS_PALINDROM = abap_false.
    endif.

ENDFUNCTION.