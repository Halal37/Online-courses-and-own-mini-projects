FUNCTION Y_JZA_FG10.
*"----------------------------------------------------------------------
*"*"Local Interface:
*"  IMPORTING
*"     REFERENCE(IN_VAL1) TYPE  I
*"     REFERENCE(IN_VAL2) TYPE  I
*"     REFERENCE(IN_VAL3) TYPE  I
*"  EXPORTING
*"     REFERENCE(OUT_VAL) TYPE  I
*"----------------------------------------------------------------------

if IN_VAL1 < IN_VAL2.
  OUT_VAL = IN_VAL1.
else.
  OUT_VAL = IN_VAL2.
endif.
if OUT_VAL > IN_VAL3.
   OUT_VAL = IN_VAL3.
endif.



ENDFUNCTION.