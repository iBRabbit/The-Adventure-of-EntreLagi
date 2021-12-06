hile check == False:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(MAX_OBS):
                if posx != obs[j].xcor() & posy != obs[j].ycor():
                    check = True
                    break