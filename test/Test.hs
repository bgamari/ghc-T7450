module Test2() where

class Hello a where
    hello :: a -> Bool

instance Hello Bool where
    hello a = a

instance Hello a => Hello [a] where
    {-# SPECIALIZE instance Hello [Bool] #-}
    {-# SPECIALIZE instance Hello [[Bool]] #-}
    hello xs = foldl (\a b->a && hello b) True xs

