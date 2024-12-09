FROM nginx:stable-perl

RUN set -x \
    && cd /etc/nginx \
    && grep -i include\.*conf nginx.conf

COPY stub_status.conf conf.d/stub_status.conf

RUN ls -la conf.d/stub_status.conf

RUN nginx -t

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]