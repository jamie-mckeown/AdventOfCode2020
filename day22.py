##############################################################################################################
class Deck :
    
    #   Initialised with the players deck, given as a list of integers
    def __init__ (self, deck) :
        self.deck = [ int(card) for card in deck ]

    #   Draw the card at the top of the deck - return it and remove it from the deck
    def draw (self) :
        card = self.deck[0] 
        self.deck.remove(card)

        return card

    #   Winner gets both cards - theirs first, then the losers
    def collect (self, winner, loser) :
        self.deck.append(winner)
        self.deck.append(loser)

    #   Boolean to check whether the deck is empty (and the game is over)
    def hascards (self):
        return True if len(self.deck) != 0 else False

    #   PART ONE GAME - takes a second Deck object for player2
    def game1 (self, other) :
        while self.hascards() and other.hascards():
            play1 = self.draw()
            play2 = other.draw()

            if play1 > play2:
                self.collect(play1, play2)
            elif play2 > play1:
                other.collect(play2, play1)

        if self.hascards():
            winners_deck = self.deck
        else:
            winners_deck = other.deck

        score = 0
        for i in range(1, len(winners_deck) + 1):
            score += i * winners_deck[-i]


        return score

    #   PART TWO GAME - take a second Deck object for player2
    def game2 (self, other):
        rounds = {} # store decks for previous round as a tuple (deck1, deck2)
        round = 1

        while self.hascards() and other.hascards():

            #   If these exact decks have appeared before, player1 (self) wins
            if (self.deck, other.deck) in rounds.values():
                break
            
            #   Otherwise play the game
            else:
                rounds[round] = (self.deck.copy(), other.deck.copy())
                round += 1

                play1 = self.draw()
                play2 = other.draw()

                #   Both players have at least as many cards remaining as the card they've dealt, thus play recursively
                if len(self.deck) >= play1 and len(other.deck) >= play2:
                    subcopy1 = self.deck[0 : play1]
                    subcopy2 = other.deck[0 : play2]

                    subplayer1, subplayer2 = Deck(subcopy1), Deck(subcopy2)

                    subwinner = subplayer1.game2(subplayer2)[0]

                    if "Player 1" in subwinner:
                        self.collect(play1, play2)

                    else:
                        other.collect(play2, play1)

                #   Otherwise play a normal round of Combat based on highest valued card
                else:
                    if play1 > play2:
                        self.collect(play1, play2)
                    elif play2 > play1:
                        other.collect(play2, play1)
        
        #   determining who won the game
        if (self.deck, other.deck) in rounds.values():
            winners_deck = self.deck
            winner_name = "Player 1"
        else:
            if self.hascards():
                winners_deck = self.deck
                winner_name = "Player 1"
            else:
                winners_deck = other.deck
                winner_name = "Player 2"

        winners_score = 0
        for i in range(1, len(winners_deck) + 1):
            winners_score += i * winners_deck[-i]


        return (winner_name, winners_deck, winners_score)


    
##############################################################################################################
#   Input puzzle
with open("day22input.txt", "r") as file:
    playerOne, playerTwo = file.read().split("\n\n")

    playerOne = playerOne.split("\n")[1:]
    playerTwo = playerTwo.split("\n")[1:]


#   PART ONE

#   Create game1 Deck instances
player1 = Deck(playerOne)
player2 = Deck(playerTwo)

#   Play Part One (game1)
print("The solution to Part One is", player1.game1(player2))


#   PART TWO - very slow

#   Clear previous game and create a new one
del player1, player2
player1, player2 = Deck(playerOne), Deck(playerTwo)

#   Play Part Two (game2)
print("The solution to Part Two is", player1.game2(player2)[2])

