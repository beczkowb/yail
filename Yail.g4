grammar Yail;

prog: ( stat? NEWLINE )* 
;

stat:  ID '=' plus_minus_expr   #assign
  | 'write' ID    #write
  | 'read' ID  #read
  | TYPE ID '=' plus_minus_expr  #declare
;


plus_minus_expr: plus_minus_expr ADD_MINUS_DELIMITER mult_div_expr   #plus_minus  
  | mult_div_expr #single_p_m
;

mult_div_expr: expression MULT_DIV_DELIMITER  mult_div_expr #mult_div
  | expression #single_m_d
;

expression: INT  #int
  | ID # id
  | DOUBLE #double
  | TOINT expression  #toint
  | TODOUBLE expression #todouble
  | '(' plus_minus_expr ')' #par
; 

TOINT: '(int)'
    ;

TODOUBLE: '(double)'
    ;

TYPE: 'int' 
    | 'double';

ID: ([a-z]|[A-Z])+
   ;

DOUBLE: [0-9]+'.'[0-9]+
    ;

INT: [0-9]+
    ;

ADD_MINUS_DELIMITER: '+'
    | '-'
    ;

MULT_DIV_DELIMITER: '*'
    | '/'
    ;


NEWLINE:  '\r'? '\n'
    ;

WS:   (' '|'\t')+ -> skip
    ;
