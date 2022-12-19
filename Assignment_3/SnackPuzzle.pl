snack(A) :-
    A = [[monday,_,_],[tuesday,_,_],[wednesday,_,_],[thursday,_,_],[friday,_,_]],
%condition 1 - The apple was eaten later than the mango
    before([_,mango,_],[_,apple,_],A),
% condition 2 - The banana was eaten later than the almonds and peanuts,
% but earlier than the orange.
    before([_,_,almonds],[_,banana,_],A),
    before([_,_,peanuts],[_,banana,_],A),
    before([_,banana,_],[_,orange,_],A),
% condition 3 - The cashews were eaten earlier than the banana and the plums, but later than the peanuts.
    before([_,_,cashews],[_,banana,_],A),
    before([_,_,cashews],[_,plums,_],A),
    before([_,_,peanuts],[_,_,cashews],A),
% condition 4 - Hazelnuts were not eaten the evening after the almonds.
    append(H,[[_,_,almonds],[_,_,_]|T],A),
    (member([_,_,hazelnuts],H);member([_,_,hazelnuts],T)),
% condition 5 - Ate walnuts one night
    member([_,_,walnuts],A),
    true.

print_snack([]).
print_snack([Head|Tail]) :-
    write(Head),
    nl,
    print_solve(Tail).

before(X,Y,Days) :-
    append(A,B,Days),
    member(X,A),
    member(Y,B).
