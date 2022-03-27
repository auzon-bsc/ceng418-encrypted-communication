def compute_public(private, generator, prime):
    return (generator ** private) % prime

def compute_shared(private, target_public, prime):
    return (target_public ** private) % prime