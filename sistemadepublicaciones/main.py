from revista import Revista
from libro import Libro
from editorial import Editorial

libro1 = Libro("el principito", 4000, 2000)
revista1 = Revista("gente- la pijita de lanata asombró a todos", 11, 3000)


publicaciones = []

publicaciones.append(libro1)
publicaciones.append(revista1)

editorial = Editorial()
editorial.mostrar_publicaciones(publicaciones)
