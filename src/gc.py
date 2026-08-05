def calculate_gc(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_percentage = ((g_count + c_count) / len(sequence)) * 100

    return gc_percentage

def calculate_at(sequence):
    a_count = sequence.count("A")
    t_count = sequence.count("T")

    at_percentage = ((a_count + t_count) / len(sequence)) * 100

    return at_percentage