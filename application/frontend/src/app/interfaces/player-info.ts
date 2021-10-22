import { GameCard } from "./game-card";

export interface PlayerInfo {
  name: string;
  sid: string;
  cards: GameCard[];
  cards_discovered: GameCard[];
  connected: boolean;
}
