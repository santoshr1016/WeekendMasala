# Colonel Oliver and his battalion were in midst of a battle against an extraterrestrial species Zomni. The Colonel has to win the battle at any cost to save all of humanity. He was short of soldiers, however, he had a very powerful weapon bazooka which could be used only once during the war.
#
# The Zomni army was divided into small troops scattered at different locations (which can be contained in a N x M battle ground). The bazooka, once launched on some troop is capable of killing all the Zomnis of that troop at a time but cannot harm any Zomni soldier in other troops.
#
# The war is coming to an end and the Colonel is about to lose. He has only one bazooka but something he knows for sure is that if he is able to kill the maximum possible soldiers with this bazooka, he and his soldiers definitely have a chance of winning the battle.
#
# So, the Colonel seeks your help in finding out the maximum number of Zomnis he can kill in one strike of the bazooka and also the total number of Zomni troops gathered against them so that he can divide his battalion efficiently (the troop killed by the bazooka should also be included).
#
# Two Zomni soldiers belong to the same troop if they are at adjacent positions in the battle ground. Therefore, any soldier who is not at some boundary of the battle ground can have a maximum of 8 adjacent soldiers.
#
# INPUT:
# First line contains single integer T, the number of test cases. First line of each test case contains two space separated integers N and M (size of the battle ground), followed by N lines containing M integers 0 or 1 where 0 means an empty space and 1 means a Zomni soldier.
#
# OUTPUT:
# For every test case, output two space separated integers X and Y where X is the number of Zomni troops and Y is the maximum number of Zomnis that can be killed by a single strike of the bazooka.
#
# CONTSTRAINTS:
# 1 ≤ T ≤ 10
# 1 ≤ N,M ≤ 1000
#
# Problem statement in native language: http://hck.re/om3VGD
# SAMPLE INPUT
#
# 2
# 4 6
# 0 0 0 1 1 0
# 1 1 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 6 4
# 1 1 1 1
# 0 0 0 0
# 0 1 0 0
# 1 0 1 0
# 1 0 0 0
# 1 0 0 0
#
# SAMPLE OUTPUT
#
# 2 4
# 2 5
#
# Explanation
#
# For the first test case
#
# there are two enemy troops first having positions 1,4 and 1,5 second having positions 2, 1 2, 2 3, 2 4, 3 Therefore the bomb should be exploded on the second troop killing all the 4 enemy soldiers.
# Time Limit: 3.0 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB
# Marking Scheme: Marks are awarded if any testcase passes.
# Allowed Languages: Bash, C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, Visual Basic
