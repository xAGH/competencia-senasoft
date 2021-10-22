import { Injectable } from '@angular/core';
import { CardStoredData } from '../interfaces/card-stored-data';

@Injectable({
  providedIn: 'root',
})
export class CardInfoService {
  constructor() {}

  private cardInfo: CardStoredData[] = [
    { id: 1, name: 'Pedro', type: 'dev', url: 'assets/avatars/PortraitPedro.png' },
    { id: 2, name: 'Juan', type: 'dev', url: 'assets/avatars/PortraitJuan.png' },
    { id: 3, name: 'Carlos', type: 'dev', url: 'assets/avatars/PortraitCarlos.png' },
    { id: 4, name: 'Juanita', type: 'dev', url: 'assets/avatars/PortraitJuanita.png' },
    { id: 5, name: 'Antonio', type: 'dev', url: 'assets/avatars/PortraitAntonio.png' },
    { id: 6, name: 'Carolina', type: 'dev', url: 'assets/avatars/PortraitCarolina.png' },
    { id: 7, name: 'Manuel', type: 'dev', url: 'assets/avatars/PortraitManuel.png' },
    { id: 8, name: 'Nómina', type: 'mod', url: 'assets/modules/ModuloNomina.jpg' },
    { id: 9, name: 'Facturación', type: 'mod', url: 'assets/modules/ModuloFacturacion.jpg' },
    { id: 10, name: 'Recibos', type: 'mod', url: 'assets/modules/ModuloRecibo.jpg' },
    { id: 11, name: 'Comprobante Contable', type: 'mod', url: 'assets/modules/ModuloComprobanteContable.jpg' },
    { id: 12, name: 'Usuarios', type: 'mod', url: 'assets/modules/ModuloUsuarios.jpg' },
    { id: 13, name: 'Contabilidad', type: 'mod', url: 'assets/modules/ModuloContabilidad.jpg' },
    { id: 14, name: '404 Not Found', type: 'err', url: 'assets/errors/Error404.jpg' },
    { id: 15, name: 'Stack Overflow', type: 'err', url: 'assets/errors/ErrorStackOverFlow.jpg' },
    { id: 16, name: 'Memory Out of Range', type: 'err', url: 'assets/errors/ErrorMemoryOutOfRange.jpg' },
    { id: 17, name: 'Null Pointer', type: 'err', url: 'assets/errors/ErrorNullPointer.jpg' },
    { id: 18, name: 'Syntax Error', type: 'err', url: 'assets/errors/ErrorSyntaxError.jpg' },
    { id: 19, name: 'Encoding Error', type: 'err', url: 'assets/errors/ErrorEncodingError.jpg' },
  ];

  getCardImageUrl(id: number) : string {
    const found = this.cardInfo.find((el) => el.id === id);
    return found?.url ?? '';
  }

  getCardTitle(id: number) {
    const found = this.cardInfo.find((el) => el.id === id);
    return found?.name ?? '';
  }

  getCardType(id: number) {
    const found = this.cardInfo.find((el) => el.id === id);
    return found?.type ?? '';
  }

  getCardInfo(id: number) {
    const found = this.cardInfo.find((el) => el.id === id);
    return found;
  }
}
