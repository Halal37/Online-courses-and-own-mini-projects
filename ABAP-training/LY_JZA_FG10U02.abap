FUNCTION Y_JZA_REVERSE10.
*"----------------------------------------------------------------------
*"*"Local Interface:
*"  IMPORTING
*"     REFERENCE(IN_TEXT) TYPE  STRING
*"  EXPORTING
*"     REFERENCE(OUT_TEXT) TYPE  STRING
*"----------------------------------------------------------------------

data lv_dlugosc type i.
data lv_znak type char01.
data lv_pos type i.

lv_dlugosc = strlen( in_text ).
lv_pos = lv_dlugosc - 1.

while lv_pos >= 0.
  lv_znak = in_text+lv_pos(1).
*  write: /'znak ', lv_znak,lv_pos.
  concatenate out_text lv_znak into out_text.
  subtract 1 from lv_pos.
  endwhile.

ENDFUNCTION.

*form odwroc_slowo using in_text type string changing out_text type string.



*endform.