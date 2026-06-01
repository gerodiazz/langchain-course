from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
information = """""Martin Charles Scorsese (Nueva York, 17 de noviembre de 1942) es un director, guionista, actor y productor de cine estadounidense.[1] Con una trayectoria que abarca más de cincuenta años, las películas de Scorsese abordan temáticas relacionadas con el catolicismo, la identidad italoestadounidense o la criminalidad,[2] caracterizándose por su violencia, uso del lenguaje vulgar, estar ambientadas en la ciudad de Nueva York y la inclusión de canciones pop, rock y clásicas en la banda sonora.[3] El origen italiano y católico de su familia, su infancia en Little Italy y su afición por el cine italiano y estadounidense de las décadas de 1940 y 1950 influyeron en su obra como cineasta.[Nota 1]

Durante su formación como cineasta y poco después de graduarse en la Universidad de Nueva York, realizó sus primeros cortometrajes y el largometraje Who's That Knocking at My Door (1967). Posteriormente, captó la atención de la crítica con la cinta de gánsteres Mean Streets (1973), donde el estilo que lo iba a caracterizar como director se hizo evidente.[Nota 2] Logró catapultarse como parte del Nuevo Hollywood dirigiendo los filmes dramáticos Taxi Driver (1976) y Toro salvaje (1980), que consolidaron su posición de prestigio gracias su éxito crítico y las candidaturas a diversos galardones, incluyendo el Óscar.[Nota 3] Durante esa época además, Robert De Niro comenzó a actuar bajo su dirección, una asociación que se iba a repetir en diez largometrajes. Después de una década de resultados desparejos, regresó a su mejor nivel como realizador con Goodfellas (1990).[6]

Aunque es conocido por dirigir cintas de gánsteres gracias a la popularidad de Goodfellas, Casino (1995) o El irlandés (2019), Scorsese ha demostrado versatilidad explorando diversos géneros.[7] Su filmografía también comprende el musical New York, New York (1977), las comedias negras El rey de la comedia (1983) y After Hours (1985), el thriller psicológico Cape Fear (1991) y el drama romántico La edad de la inocencia (1993). Su carrera tampoco estuvo exenta de controversias, como la desatada a partir de su retrato de Jesús en La última tentación de Cristo (1988) o la censura sufrida por Kundun (1997) de parte del gobierno comunista chino.[Nota 4] Hacia el comienzo del nuevo milenio sus producciones comenzaron a contar con mayores presupuestos, acompañados en algunos casos de éxitos comerciales sin precedentes en su carrera.[10] El drama histórico Gangs of New York (2002) marcó el comienzo de su colaboración con Leonardo DiCaprio, quien actuó en seis de sus largometrajes, incluyendo la película biográfica El aviador (2004), el thriller policíaco The Departed (2006), el thriller psicológico Shutter Island (2010) y la sátira de humor negro El lobo de Wall Street (2013). Además dirigió el drama de aventuras Hugo (2011) y el drama histórico Silencio (2016).

Tras repetidas nominaciones, Scorsese ganó el Óscar al mejor director gracias a su trabajo en The Departed (2006). Con diez candidaturas al Óscar como mejor director,[11] es el director vivo con más nominaciones en esa categoría y el segundo en la historia.[12] Además del Óscar, se ha hecho acreedor de múltiples galardones, entre ellos los premios Globo de Oro, BAFTA, Primetime Emmy, SAG, Palma de Oro, el premio del Festival de Cannes al mejor director y el León de Plata a la mejor dirección. El impacto de su cine en la cultura lo ha llevado a transformarse en uno de los directores más influyentes y es, en opinión del crítico de cine Roger Ebert, el «mejor director estadounidense en actividad».[13] Varias de sus películas han sido seleccionadas entre las mejores de todos los tiempos por organizaciones como el American Film Institute o las revistas Sight and Sound y Empire.[Nota 5]

Su labor no está limitada a la dirección de largometrajes de ficción. En sus inicios consiguió trabajos como montador, participando en la realización del documental Woodstock (1970),[18] y resultó seleccionado por su mentor John Cassavetes para trabajar como asistente de edición de sonido en Minnie and Moskowitz (1971).[19] Trabajando para la televisión, fue director ejecutivo y dirigió los episodios piloto de las series de HBO Boardwalk Empire (2010) y Vinyl (2016). Como aficionado a la música, ha dirigido una amplia gama de documentales relacionados con el tema, incluyendo The Last Waltz (1978), considerado por algunos críticos como uno de los mejores documentales de música de todos los tiempos.[20] También dirigió No Direction Home (2005), Shine a Light (2008), George Harrison: Living in the Material World (2011) y Rolling Thunder Revue: A Bob Dylan Story by Martin Scorsese (2019). Asimismo, parte de sus esfuerzos están dedicados a la preservación de películas mediante The Film Foundation, una organización fundada con dichos fines en 1990.[21][22
    
    
    """
summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """
summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template)

# llm = ChatOpenAI(temperature=0, model="gpt-5")
llm = ChatOllama(temperature=0, model="llama3.2:3b")
chain = summary_prompt_template | llm
response = chain.invoke(input={"information": information})
print(response.content)
if __name__ == "__main__":
    main()
