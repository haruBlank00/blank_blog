import Alpine from 'alpinejs';
import '../styles/styles.css';

declare global {
    interface Window {
        Alpine: typeof Alpine
    }
}

window.Alpine = Alpine;

Alpine.start()