def calculate_gc(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_percentage = ((g_count + c_count) / len(sequence)) * 100

    return gc_percentage