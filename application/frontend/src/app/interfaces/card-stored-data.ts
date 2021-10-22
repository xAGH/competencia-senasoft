import { GameCard } from "./game-card";

export interface CardStoredData extends GameCard {
  url: string;
}
