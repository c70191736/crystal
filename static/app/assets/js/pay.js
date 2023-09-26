const paymentForm =  document.getElementById('paymentForm');
paymentForm.addEventListener('submit', payWithPaystack, false);
function payWithPaystack(e) {
    e.preventDefault();

    let handler = PaystackPop.setup({
            key:'pk_live_67a55089e4829715b7fe2a879ce7da74297cb8a0',
            email: '{{request.user.email}}',
            amount:'{{ post.amount }}' * 100,
            currency:'NGN',
            ref:'ccity'+Math.floor((Math.random() * 1000000000) + 1),

            onClose: function()
            {
                alert('Transaction was not completed, Window closed.');
            },

            callback: function(response)
            {
                a = document.getElementById('btnDownload');
                a.click();
                let message = 'Payment complete!';
                alert(message);
            },

        });

        handler.openIframe();
}