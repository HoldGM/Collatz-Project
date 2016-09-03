#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#-------------
# global cache
#-------------

eager_cache = [144, 179, 182, 180, 209, 217, 199, 238, 215, 210, 192, 236, 262, 257, 239, 252, 234, 247, 260, 242, 255, 268, 237, 250, 263, 263, 
        276, 258, 209, 271, 271, 253, 266, 266, 235, 279, 248, 261, 212, 274, 243, 256, 256, 269, 269, 269, 251, 282, 251, 264, 264, 233, 
        277, 308, 259, 259, 259, 228, 272, 272, 272, 254, 285, 285, 267, 267, 267, 267, 311, 280, 311, 324, 249, 231, 262, 306, 244, 244, 
        275, 306, 275, 288, 244, 257, 288, 257, 257, 270, 270, 270, 314, 239, 283, 252, 314, 283, 252, 296, 265, 296, 265, 278, 309, 247, 
        278, 340, 322, 247, 260, 260, 260, 260, 322, 291, 304, 273, 242, 273, 273, 304, 317, 335, 286, 317, 255, 286, 330, 255, 299, 268, 
        224, 268, 268, 237, 268, 312, 312, 237, 281, 299, 312, 312, 325, 250, 263, 263, 294, 294, 294, 325, 307, 294, 307, 307, 351, 245, 
        307, 338, 307, 307, 320, 276, 320, 289, 307, 320, 258, 289, 320, 289, 289, 302, 302, 227, 333, 271, 333, 271, 315, 302, 315, 271, 
        333, 253, 284, 315, 284, 253, 284, 315, 328, 284, 297, 253, 297, 297, 266, 284, 328, 328, 341, 266, 297, 310, 310, 310, 235, 248, 
        297, 310, 341, 310, 354, 323, 292, 279, 279, 261, 292, 310, 292, 292, 323, 292, 323, 305, 261, 292, 305, 261, 305, 349, 230, 305, 
        274, 305, 336, 318, 305, 305, 318, 243, 274, 336, 256, 318, 331, 318, 287, 256, 318, 287, 318, 331, 287, 287, 331, 331, 300, 344, 
        300, 331, 300, 287, 331, 331, 313, 313, 269, 300, 344, 282, 313, 313, 331, 251, 313, 282, 313, 251, 344, 313, 282, 326, 300, 375, 
        282, 282, 326, 295, 264, 295, 295, 357, 264, 295, 295, 326, 233, 326, 370, 295, 264, 295, 308, 264, 308, 308, 352, 308, 308, 246, 
        383, 308, 277, 339, 321, 308, 352, 308, 370, 290, 277, 290, 321, 339, 246, 321, 290, 334, 321, 290, 352, 303, 321, 290, 321, 303, 
        334, 259, 290, 290, 334, 334, 303, 303, 347, 321, 334, 303, 241, 272, 334, 303, 334, 316, 347, 303, 303, 303, 365, 316, 241, 316, 
        316, 334, 254, 254, 316, 285, 329, 316, 316, 347, 329, 316, 316, 285, 316, 360, 329, 285, 254, 329, 329, 347, 329, 298, 329, 342, 
        360, 329, 236, 298, 267, 285, 329, 329, 329, 298, 342, 311, 267, 311, 342, 342, 311, 267, 311, 311, 355, 329, 342, 373, 311, 311, 
        280, 311, 311, 280, 342, 324, 355, 311, 355, 324, 280, 373, 293, 280, 280, 280, 386, 342, 324, 249, 324, 262, 337, 355, 324, 249, 
        355, 337, 262, 324, 324, 262, 324, 231, 368, 293, 262, 368, 306, 262, 355, 275, 262, 306, 306, 443, 350, 324, 337, 293, 368, 275, 
        381, 337, 306, 275, 337, 306, 350, 319, 306, 275, 350, 306, 293, 368, 275, 275, 319, 288, 319, 337, 257, 275, 257, 319, 257, 332, 
        350, 319, 257, 288, 350, 332, 332, 319, 319, 257, 319, 288, 306, 332, 288, 363, 288, 288, 257, 332, 345, 257, 288, 301, 270, 345, 
        319, 332, 332, 288, 301, 270, 407, 288, 332, 332, 270, 332, 301, 314, 345, 301, 270, 257, 345, 345, 407, 363, 283, 270, 270, 314, 
        283, 358, 332, 314, 345, 252, 314, 314, 283, 389, 345, 314, 314, 283, 345, 327, 358, 327, 314, 314, 358, 327, 283, 358, 376, 296, 
        283, 314, 327, 283, 389, 389, 345, 327, 252, 327, 327, 265, 340, 296, 358, 327, 252, 296, 358, 265, 327, 296, 327, 327, 265, 371, 
        327, 234, 371, 340, 296, 296, 265, 340, 327, 340, 340, 309, 265, 265, 309, 309, 278, 309, 371, 327, 309, 340, 371, 371, 309, 278, 
        384, 353, 340, 309, 278, 278, 340, 278, 322, 353, 309, 309, 309, 353, 322, 278, 353, 371, 353, 278, 247, 309, 322, 291, 322, 384, 
        340, 322, 247, 247, 322, 322, 260, 291, 353, 353, 291, 322, 247, 291, 353, 335, 322, 335, 322, 291, 322, 322, 366, 322, 247, 366, 
        335, 291, 260, 366, 291, 304, 304, 335, 335, 353, 335, 304, 291, 304, 304, 441, 304, 348, 322, 304, 335, 260, 291, 366, 304, 273, 
        379, 348, 335, 335, 304, 229, 348, 335, 379, 379, 348, 304, 304, 273, 379, 348, 317, 348, 410, 366, 348, 273, 361, 273, 273, 317, 
        286, 317, 361, 335, 286, 348, 286, 255, 317, 317, 348, 361, 392, 304, 348, 317, 317, 286, 286, 348, 317, 330, 361, 330, 317, 423, 
        286, 361, 330, 317, 361, 361, 379, 299, 286, 374, 361, 317, 330, 299, 330, 330, 348, 343, 330, 255, 268, 299, 330, 299, 436, 361, 
        299, 361, 330, 330, 299, 286, 299, 361, 255, 405, 312, 299, 330, 299, 330, 268, 374, 330, 299, 299, 374, 343, 387, 299, 268, 268, 
        255, 343, 330, 343, 405, 281, 361, 343, 268, 268, 299, 312, 312, 281, 449, 374, 312, 330, 312, 343, 268, 374, 312, 374, 312, 281, 
        387, 343, 343, 312, 343, 312, 237, 281, 343, 312, 325, 281, 356, 325, 312, 418, 281, 356, 325, 356, 281, 356, 356, 374, 294, 281, 
        281, 281, 312, 281, 325, 343, 325, 387, 268, 343, 338, 356, 250, 281, 325, 325, 387, 263, 294, 400, 325, 356, 294, 325, 263, 294, 
        294, 356, 325, 338, 281, 325, 338, 325, 294, 325, 263, 325, 369, 338, 369, 294, 369, 387, 307, 294, 276, 294, 369, 294, 338, 325, 
        263, 338, 338, 356, 276, 338, 307, 263, 294, 307, 307, 276, 444, 307, 369, 307, 325, 307, 338, 338, 369, 307, 369, 369, 307, 413, 
        382, 351, 307, 338, 307, 307, 276, 276, 276, 338, 307, 294, 382, 351, 320, 276, 307, 307, 382, 307, 351, 338, 320, 351, 413, 294, 
        369, 382, 351, 276, 258, 307, 276, 320, 320, 338, 320, 382, 382, 338, 382, 320, 351, 276, 320, 320, 320, 320, 276, 426, 320, 395, 
        307, 351, 320, 320, 320, 258, 289, 289, 351, 289, 333, 395, 364, 333, 320, 320, 426, 320, 271, 320, 364, 320, 289, 364, 364, 382, 
        333, 364, 333, 377, 302, 364, 289, 333, 320, 470, 289, 333, 333, 351, 346, 364, 395, 302, 271, 302, 333, 333, 302, 439, 258, 364, 
        302, 333, 364, 333, 302, 333, 271, 302, 302, 364, 364, 408, 408, 333, 377, 346, 333, 377, 333, 302, 271, 346, 346, 333, 302, 377, 
        377, 320, 346, 315, 284, 302, 333, 302, 377, 346, 346, 333, 315, 346, 346, 408, 364, 346, 284, 346, 315, 359, 302, 315, 315, 346, 
        284, 452, 315, 377, 315, 333, 253, 315, 346, 346, 284, 377, 315, 315, 315, 346, 421, 284, 390, 359, 315, 346, 315, 315, 315, 253, 
        284, 284, 359, 346, 315, 328, 284, 359, 328, 284, 315, 421, 328, 284, 266, 359, 359, 346, 315, 359, 271, 359, 377, 284, 297, 359, 
        284, 372, 315, 359, 315, 328, 328, 346, 284, 390, 390, 271, 346, 315, 359, 328, 253, 266, 328, 297, 328, 328, 328, 434, 372, 359, 
        359, 328, 359, 328, 297, 328, 297, 315, 297, 297, 359, 359, 328, 403, 297, 328, 328, 297, 328, 297, 266, 328, 372, 266, 341, 372, 
        341, 297, 372, 253, 372, 297, 403, 385, 279, 297, 279, 297, 372, 297, 341, 310, 328, 297, 341, 341, 403, 266, 359, 279, 341, 341, 
        354, 266, 297, 310, 310, 310, 310, 279, 447, 310, 372, 310, 328, 372, 248, 310, 341, 266, 266, 372, 279, 372, 310, 310, 310, 354, 
        341, 385, 354, 310, 509, 310, 310, 341, 279, 235, 279, 279, 341, 310, 310, 279, 385, 279, 354, 323, 310, 310, 279, 416, 279, 310, 
        354, 354, 354, 341, 279, 354, 354, 416, 261, 372, 416, 354, 279, 279, 261, 279, 310, 310, 323, 323, 310, 341, 279, 323, 385, 323, 
        341, 336, 336, 323, 354, 354, 336, 385, 323, 323, 323, 385, 354, 429, 323, 354, 398, 323, 310, 354, 323, 292, 323, 292, 261, 292, 
        292, 292, 367, 323, 442, 398, 323, 323, 367, 336, 292, 323, 292, 336, 323, 323, 323, 323, 367, 261, 336, 292, 367, 248, 367, 385, 
        336, 305, 292, 336, 261, 380, 292, 367, 336, 336, 336, 336, 305, 305, 336, 380, 336, 261, 354, 261, 274, 398, 367, 380, 261, 292, 
        336, 336, 336, 336, 274, 442, 305, 323, 367, 305, 274, 367, 274, 336, 305, 336, 318, 261, 367, 305, 305, 367, 367, 305, 305, 411, 
        274, 380, 349, 305, 336, 504, 380, 336, 305, 274, 274, 349, 274, 349, 336, 305, 380, 292, 380, 274, 349, 411, 305, 380, 305, 274, 
        305, 305, 380, 336, 349, 349, 336, 318, 305, 349, 261, 411, 292, 367, 411, 380, 349, 274, 256, 362, 287, 305, 318, 349, 318, 318, 
        287, 362, 287, 318, 380, 380, 318, 336, 380, 287, 318, 349, 349, 287, 380, 424, 318, 318, 380, 318, 349, 424, 424, 318, 393, 362, 
        318, 318, 349, 318, 287, 318, 318, 300, 256, 349, 287, 287, 349, 362, 318, 274, 393, 287, 362, 318, 331, 318, 318, 305, 424, 331, 
        287, 318, 362, 362, 362, 349, 331, 318, 362, 362, 362, 305, 380, 331, 300, 362, 256, 331, 375, 318, 287, 362, 318, 331, 331, 300, 
        318, 468, 300, 331, 393, 393, 331, 349, 344, 269, 362, 393, 362, 331, 256, 331, 437, 300, 331, 300, 393, 269, 437, 300, 331, 362, 
        344, 300, 331, 362, 287, 331, 300, 331, 300, 313, 300, 375, 300, 300, 362, 362, 406, 300, 406, 300, 331, 375, 344, 331, 300, 437, 
        375, 269, 331, 300, 331, 269, 468, 375, 344, 344, 300, 300, 375, 375, 375, 282, 393, 406, 388, 282, 300, 269, 331, 313, 331, 375, 
        300, 344, 406, 238, 331, 313, 300, 344, 406, 406, 287, 251, 362, 344, 375, 344, 269, 313, 357, 344, 282, 344, 313, 344, 344, 450, 
        300, 357, 450, 313, 313, 375, 344, 331, 331, 375, 326, 313, 313, 344, 313, 282, 375, 419, 282, 313, 375, 375, 344, 251, 419, 357, 
        282, 388, 344, 357, 313, 344, 295, 313, 313, 344, 313, 525, 282, 344, 282, 388, 357, 344, 313, 313, 269, 388, 331, 282, 357, 357, 
        401, 313, 313, 282, 419, 326, 282, 313, 313, 357, 357, 357, 357, 344, 326, 313, 357, 269, 419, 300, 264, 388, 357, 375, 357, 282, 
        282, 370, 313, 295, 357, 326, 313, 326, 326, 326, 313, 344, 295, 326, 388, 388, 326, 251, 344, 326, 339, 357, 388, 357, 326, 295, 
        282, 432, 326, 326, 326, 326, 388, 357, 264, 432, 370, 326, 401, 357, 295, 326, 326, 357, 326, 295, 295, 326, 295, 313, 264, 370, 
        295, 295, 370, 326, 357, 445, 282, 401, 295, 264, 370, 370, 339, 326, 295, 326, 295, 264, 326, 295, 295, 370, 264, 326, 339, 370, 
        339, 326, 339, 370, 295, 251, 370, 401, 388, 401, 308, 383, 277, 295, 264, 383, 264, 295, 445, 339, 326, 295, 370, 339, 326, 308, 
        476, 295, 339, 383, 401, 401, 264, 357, 339, 370, 339, 339, 339, 308, 383, 339, 277, 339, 339, 432, 339, 339, 339, 277, 277, 445, 
        308, 308, 370, 339, 308, 339, 326, 370, 476, 308, 383, 339, 339, 339, 326, 370, 308, 277, 308, 370, 339, 370, 414, 308, 414, 277, 
        321, 383, 339, 352, 445, 308, 507, 308, 383, 277, 339, 308, 277, 339, 277, 352, 383, 352, 352, 339, 352, 383, 383, 277, 383, 326, 
        277, 352, 308, 414, 383, 308, 414, 277, 414, 308, 277, 383, 308, 339, 352, 352, 352, 339, 321, 321, 277, 352, 352, 414, 352, 290, 
        370, 383, 414, 383, 352, 259, 277, 321, 365, 308, 308, 308, 321, 308, 352, 321, 321, 458, 352, 339, 277, 321, 321, 383, 383, 334, 
        321, 339, 383, 259, 334, 321, 383, 352, 321, 334, 259, 427, 321, 321, 321, 383, 383, 383, 352, 321, 427, 365, 321, 352, 396, 352, 
        321, 308, 321, 352, 321, 321, 321, 321, 321, 352, 290, 259, 365, 290, 290, 365, 365, 352, 352, 440, 277, 396, 396, 290]

lazy_cache = dict()

# ------------
# collatz_read
# ------------

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    try:
        if i == 0 or j == 0 or i > 1000000 or j > 1000000:
            raise IOError('Invalid Input')
        maxCycles = 0
        if i > j:
            temp = i
            i = j
            j = temp
        if i < (j //2):
            i = j // 2

        interval = j - i
        x = i
        while x <= j:
            if x % 500 == 1 and interval >= 500:
                interval_cycle_count = eager_cache[x // 500]
                if interval_cycle_count > maxCycles:
                    maxCycles = interval_cycle_count
                x += 500
                interval -= 500
                continue
            if x in lazy_cache:
                cycleCount = lazy_cache[x]
                if cycleCount > maxCycles:
                    maxCycles = cycleCount
            t = x
            cycleCount = 1
            while t > 1:
                if t in lazy_cache:
                    cycleCount += lazy_cache[t] - 1
                    lazy_cache[x] = cycleCount
                    break
                if t % 2 == 0:
                    t = t / 2
                else:
                    t = t * 3 + 1
                cycleCount += 1
                
            if cycleCount > maxCycles:
                maxCycles = cycleCount
                lazy_cache[x] = cycleCount
            x += 1
            interval -= 1
        return maxCycles
    except IOError as e:
        return "Invalid Input"
# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(u"" + str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):

    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        # print(str(i) + " " + str(j))
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

