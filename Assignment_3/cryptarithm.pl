:- use_module(library(clpfd)).

logic_four([T,W,O] + [T,W,O] = [F,O,U,R]) :-
        Vars = [F,T,U,W,R,O],
        Vars ins 0..9,
        all_different(Vars),
        O+O #= R+10*X1,
        X1+W+W #= U+10*X2,
        X2+T+T #= O+10*X3,
        X3 #=F, F #\= 0, T #\= 0,
        label(Vars).
