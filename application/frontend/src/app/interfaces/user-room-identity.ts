import { PlayerInfo } from "./player-info";
import { SocketMessage } from "./socket-message";

export interface UserRoomIdentity extends SocketMessage {
  users: PlayerInfo[];
  you: PlayerInfo;
}
